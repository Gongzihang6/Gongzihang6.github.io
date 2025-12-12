# PointMamba: A Simple State Space Model for Point Cloud Analysis

主要是为了解决 PointTransformers 的自注意力机制的二次复杂度问题，提高模型运算效率，解决点云数量增加时带来的计算消耗和显存占用明显增加的问题；

### 1. 核心公式回顾

标准自注意力机制的计算公式为：

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)V$$

**变量定义：**

-   $N$：序列长度（在点云任务中为点数，Point Tokens 的长度）。
-   $d$：隐藏层维度（特征维度）。
-   $Q, K, V$：查询、键、值矩阵，维度均为 $[N, d]$。

### 2. 时间复杂度推导

时间复杂度主要取决于两次矩阵乘法运算。

#### **第一步：计算相关性分数（Attention Scores）**

计算 $QK^T$：

-   矩阵 $Q$ 的维度为 $[N, d]$。
-   矩阵 $K^T$ 的维度为 $[d, N]$。
-   **运算过程**：为了得到输出矩阵 $[N, N]$ 中的每一个元素，需要计算两个长度为 $d$ 的向量的点积。输出矩阵共有 $N^2$ 个元素。
-   **复杂度**：$O(N^2 \cdot d)$。

#### **第二步：加权求和（Weighted Sum）**

计算 $\text{Score} \times V$（忽略 Softmax 的 $O(N^2)$ 开销）：

-   注意力分数矩阵（经过 Softmax 后）的维度为 $[N, N]$。
-   矩阵 $V$ 的维度为 $[N, d]$。
-   **运算过程**：为了得到输出矩阵 $[N, d]$ 中的每一个元素，需要进行长度为 $N$ 的向量点积运算。输出矩阵共有 $N \cdot d$ 个元素。
-   **复杂度**：$O(N \cdot N \cdot d) = O(N^2 \cdot d)$。

#### **总时间复杂度**

将上述两步相加：

$$O(N^2 d) + O(N^2 d) = O(N^2 d)$$

>   Transformer 的注意力机制具有二次方复杂度（quadratic complexity），具体公式为 $O(N^2d)$，这意味着随着输入序列长度 $N$ 的增加，运算效率会受到显著限制 。

### 3. 空间复杂度推导

空间复杂度主要来源于存储中间计算结果（显存占用），用于反向传播时的梯度计算。

#### **主要瓶颈：注意力图（Attention Map）**

-   在计算 $QK^T$ 后，生成的注意力分数矩阵维度为 $[N, N]$。
-   为了在反向传播中更新权重，必须在显存中保存这个 $N \times N$ 的矩阵。
-   **复杂度**：$O(N^2)$。

#### **其他部分**

-   存储输入输出 $Q, K, V$ 及最终结果：$O(Nd)$。
-   由于通常序列长度 $N$ 远大于特征维度 $d$（例如在点云处理中 $N$ 可达数万），因此 $N^2$ 项占主导地位。

#### **总空间复杂度**

$$O(N^2) + O(Nd) \approx O(N^2)$$

>   由于注意力机制的二次方复杂度，导致计算成本高昂，对低资源设备不友好 2。相比之下，PointMamba 展示了显著降低的 GPU 内存使用率（例如在序列长度增加时，PointMamba 的显存占用比 Point-MAE 低 24.9 倍）3。

### 4. 总结与对比

| **维度** | **复杂度** | **说明**                                                     |
| -------- | ---------- | ------------------------------------------------------------ |
| **时间** | $O(N^2 d)$ | 随序列长度 $N$ 呈二次方增长，导致处理大规模点云（Large $N$）时速度极慢。 |
| **空间** | $O(N^2)$   | 需要存储 $N \times N$ 的注意力矩阵，容易导致显存溢出（OOM）。 |

PointMamba 的优势：PointMamba 利用 Mamba（状态空间模型 SSM）将上述复杂度降低为 线性复杂度：

-   **时间复杂度**：$O(N)$（或更准确地说是 $O(N \cdot d)$，与序列长度线性相关）。

-   **结果**：在长序列（如 $N=32768$）下，PointMamba 的推理速度比 Transformer 基线（Point-MAE）快 30.2 倍，FLOPs 降低 5.2 倍 。

---

### **PointMamba 数据流转全解析**

#### **0. 初始状态：数据输入 (Input)**

-   **数据形态**：假设我们输入一个点云 $P$，包含 $M$ 个点，每个点有 $(x, y, z)$ 三维坐标。
-   **数学表示**：$P \in \mathbb{R}^{M \times 3}$ 1。
    -   注：在实验设置中，通常 $M=1024$（ModelNet40）或 $M=2048$（ScanObjectNN）。对于原始输入点云，点数一般远超 1024 或者 2048，通常采用随机下采样到 $M$。
-   **数据增强 (Data Augmentation)**：在预处理阶段，可能会对点云进行简单的缩放（Scale）、平移（Translation）或旋转（Rotation）以增强模型的鲁棒性。

------

#### **1. 关键点采样 (Farthest Point Sampling, FPS)**

-   **功能**：从原始密集的点云中选取最具代表性的骨架点，降低计算量同时保留几何结构。
-   **过程描述**：使用最远点采样算法（FPS）。首先随机选择一个点，然后迭代选择距离已选点集最远的点，直到选出 $G$ 个点。
-   **数学表示**：$FPS(P) \rightarrow p$
-   **形状变化**：$M \times 3 \rightarrow G \times 3$ 。
    -   注：论文中通常设定 $G=64$ 或 $128$ 个中心点（Patches）。

------

#### **2. 序列化策略 (Serialization via Space-Filling Curves)**

-   **功能**：这是 PointMamba 的核心创新之一。由于 Mamba（SSM）是处理序列数据的（如文本），而点云是无序的 3D 数据，必须将其“拉直”成 1D 序列。

-   **过程描述**：

    1.  **Hilbert 曲线扫描**：将 3D 空间划分为网格，利用 Hilbert 曲线遍历这些网格，根据点在曲线上的位置给予索引并排序，得到序列 $p_h$ 。
    2.  **Trans-Hilbert 曲线扫描**：利用 Hilbert 曲线的变体（例如坐标轴置换）再次扫描，得到另一种顺序的序列 $p_{h'}$ 。

    -   >   *目的*：两种扫描提供了互补的几何视角，弥补 Mamba 单向建模的局限性。

-   **形状变化**：数据形状保持不变，但点的 **排列顺序** 变了。

    -   序列 A：$G \times 3$ (按 Hilbert 排序)
    -   序列 B：$G \times 3$ (按 Trans-Hilbert 排序) 。

------

#### **3. 局部特征聚合 (KNN & Patching)**

-   **功能**：单纯的一个点信息太少，需要聚合其周围邻居的信息形成“局部补丁（Patch）”。

-   **过程描述**：

    1.  对于序列中的每一个中心点，使用 K-近邻算法（K-Nearest Neighbors, KNN）在原始点云中找到最近的 $k$ 个点。

    2.  **归一化**：将邻居点的坐标减去中心点坐标，得到相对坐标，消除平移影响 。


-   数学表示：形成两个张量 $T_h$ 和 $T_{h'}$。

    $T_h \in \mathbb{R}^{G \times k \times 3}$，其中 $k$ 是邻居数量（论文中设为 32）。

-   **形状变化**：$G \times 3 \rightarrow G \times k \times 3$（两组）。

------

#### **4. Token 嵌入 (Token Embedding Layer)**

-   **功能**：将几何坐标映射到高维特征空间，类似于 NLP 中的 Word Embedding。

-   **实现**：使用一个轻量级的 **PointNet**。

    -   对每个补丁内的 $k$ 个点，通过 MLP（多层感知机）升维。
    -   通过最大池化（Max Pooling）聚合 $k$ 个点的特征，得到该补丁的唯一特征向量。
    
-   数学表示：

    $E_0^h = \text{PointNet}(T_h)$

    $E_0^{h'} = \text{PointNet}(T_{h'})$

-   **形状变化**：$G \times k \times 3 \rightarrow G \times C$。

    -   这里 $C$ 是特征维度（例如 384）。此时我们有了两个长度为 $G$ 的特征序列。

另外，还有一个位置编码过程，将每个局部补丁的中心坐标（也就是 FPS 采样得到的关键点坐标）映射为一个 $C$ 维向量，用于表示补丁的位置信息，作为残差连接，和Point tokenization之后的特征进行拼接；

------

#### **5. 顺序指示器 (Order Indicator)**

-   **功能**：告诉模型哪一部分序列是 Hilbert 排序，哪一部分是 Trans-Hilbert 排序。如果不加区分直接拼接，模型可能会混淆空间关系。

-   **过程描述**：为每种序列学习一个缩放因子（Scale, $\gamma$）和偏移因子（Shift, $\beta$）。

-   数学公式：

    $$Z_0^h = E_0^h \odot \gamma_h + \beta_h$$

    $$Z_0^{h'} = E_0^{h'} \odot \gamma_{h'} + \beta_{h'}$$

    其中 $\odot$ 是逐元素乘法。

-   拼接 (Concatenation)：将两个序列首尾相接。

    $$Z_0 = \text{Concat}(Z_0^h, Z_0^{h'})$$

-   **形状变化**：两个 $G \times C$ 的序列拼接为一个长序列 $\rightarrow 2G \times C$ 。

    -   *关键点*：现在输入 Mamba 的是一个长度为 $2G$ 的 1D 序列。

------

#### **6. Vanilla Mamba Block (核心处理单元)**

-   **架构概览**：输入序列 $Z$ 将通过 $N$ 个堆叠的 Mamba 块（论文中 $N=12$）16。虽然论文称其为“Vanilla”（原味/普通）Mamba 块，但其内部机制非常精妙。

我们将深入 Mamba 块内部，追踪数据流 $Z_{in} \in \mathbb{R}^{2G \times C}$：

**A. 归一化与线性投影 (Norm & Linear Projections)**

-   首先经过层归一化（Layer Norm）。

-   然后分为两个分支（类似于 Gated MLP）：

    -   **主分支 (Main Branch)**：$x = \text{Linear}(Z_{in})$。维度通常扩展 $E$ 倍（例如 $E=2$），形状变为 $2G \times (E \cdot C)$。

    -   **门控分支 (Gating Branch)**：$z = \text{Linear}(Z_{in})$。同样扩展，形状 $2G \times (E \cdot C)$。随后经过 SiLU 激活函数。

![PointMamba 整体网络架构图](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/2025%5C11%5Cimage-20251127103659717.png)

**B. 深度卷积 (Depth-wise Conv)**

-   **主分支** 接着通过一个 1D 深度卷积层。

-   **作用**：捕捉极局部的上下文信息（类似于 CNN 的感受野），为后续的 SSM 做局部特征准备。

-   激活：卷积后接 SiLU 激活函数。$$x' = \text{SiLU}(\text{DWConv}(x))$$


**C. 选择性状态空间模型 (Selective SSM - S6) <-- 核心中的核心**

这是 Mamba 区别于 Transformer 的地方。

1.  **离散化 (Discretization)**：

    -   SSM 的连续方程是 $h'(t) = Ah(t) + Bx(t)$。

    -   在 Mamba 中，参数 $A$ 是固定的，但 $B, C$ 和步长 $\Delta$ 是 **根据输入动态计算的**（即 Selective 机制）。

    -   对于序列中的每个 token $x_t$（这里是第 $t$ 个补丁的特征）：

        $$\Delta_t = \text{Softplus}(\text{Linear}(x_t))$$

        $$B_t = \text{Linear}(x_t)$$

        $$C_t = \text{Linear}(x_t)$$

    -   使用零阶保持（ZOH）将连续参数转化为离散参数 $\bar{A}, \bar{B}$ 。

2.  **递归/扫描 (Scan)**：

    -   模型维护一个隐状态 $h_t \in \mathbb{R}^{N_{state}}$（这里的 $N_{state}$ 是 SSM 的内部状态维度，不同于点数 $n$）。

    -   状态更新公式：

        $$h_t = \bar{A}_t h_{t-1} + \bar{B}_t x'_t$$

        $$y_t = C_t h_t$$

    -   **物理意义**：

        -   当处理序列的前半部分（Hilbert 序列）时，隐状态 $h$ 积累了点云的特征。

        -   当处理序列的后半部分（Trans-Hilbert 序列）时，由于 Mamba 的递归性质，隐状态 $h$ 依然保留着前半部分的信息。

        -   **这就是全局建模的原理**：Trans-Hilbert 部分的计算实际上利用了 Hilbert 部分积累的全局上。

3.  **输出**：SSM 输出 $y_{ssm}$，形状保持为 $2G \times (E \cdot C)$。

**D. 门控与输出投影 (Gating & Output Projection)**

-   将 SSM 的输出与门控分支的输出进行逐元素相乘：$$Z_{out} = y_{ssm} \odot z$$

-   最后通过一个线性层将维度从 $E \cdot C$ 降回 $C$。

-   残差连接：加上原始输入 $Z_{in}$。$$Z_{block\_out} = \text{Linear}(Z_{out}) + Z_{in}$$


#### **7. 任务头 (Task Head)**

-   经过 $N$ 层 Mamba 块后，我们得到了包含丰富上下文信息的序列特征 $Z_{final} \in \mathbb{R}^{2n \times C}$。
-   **池化 (Pooling)**：通常对序列进行最大池化（Max Pooling）或平均池化，将 $2n$ 个 token 的特征压缩为一个全局特征向量 $V_{global} \in \mathbb{R}^{C}$（分类任务）。
    -   注：对于分割任务（Segmentation），会保留所有 token 特征并上采样回原始点数 24242424。
-   **分类/分割**：通过全连接层（MLP）输出最终的类别概率或逐点标签。

### **总结数据流**

1.  **Input**: $M \times 3$ (无序点云)
2.  **FPS**: $\rightarrow G \times 3$ (稀疏骨架)
3.  **Serialization**: $\rightarrow$ 两个 $G \times 3$ 序列 (排序后)
4.  **KNN+Embedding**: $\rightarrow$ 两个 $G \times C$ 特征序列
5.  **Indicator+Concat**: $\rightarrow 2G \times C$ (长序列)
6.  **Mamba Encoder**: $\rightarrow 2G \times C$ (特征深度融合，前半段信息流向后半段)
7.  **Head**: $\rightarrow$ 类别/分割结果

这就是 PointMamba 处理点云数据的完整生命周期。

---

代码主体网络模型架构在models/point_mamba_scan.py中定义，封装套娃结构如下：

PointMambaScan（核心类，定义网络模型架构）**····》**MixerModel（Mamba主干网络，串联多个Mamba块）**····》**self.layers（定义串联的多个Mamba块） **····》**creat_block **····》**Block **····》**mixer_cls **····》**Mamba（这才到了Mamba块的源代码，在编译下载好的mamba_ssm包中的mamba_simple.py）**····》**selective_scan_fn **····》**SelectiveScanFn.apply/forward