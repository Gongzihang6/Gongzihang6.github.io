# Swin3D: A Pretrained Transformer Backbone  

# for 3D Indoor Scene Understanding

论文核心是提出了一个应用在 3D 点云领域的预训练 Backbone，将原先应用在 2D 图像领域的 Swin Transformer 适配到了 3D 点云，但是直接扩展会有内存耗费大，效果并不够好的问题，论文中通过优化注意力的内存占用到线性复杂度，以及点云位置的不确定性，点可能在其占据的体素内的任意位置都有可能；



Swin3D 的核心仍然是窗口注意力，借鉴了 2D Swin Transformer 的设计理念，通过分层结构和移动窗口注意力机制来高效处理 3D 点云数据

Swin3D 的整体架构分为 5 个阶段（Stages），形成了一个层级式的特征提取器。

-   输入数据：原始 3D 点云，包含点的位置 P 和其他信号（如 RGB 颜色、法向量等），表示为 $s_p \in \mathbb{R}^m$；对于颜色、法向量等成分，都要归一化到 $[-1,1]$，常用设置为 m = 6，包含 3D 点坐标和 RGB 颜色分量；
-   核心流程：`Voxelization` $\to$ `Stage-1` $\to$ `Downsample` $\to$ `Stage-2` ... $\to$ `Stage-5`。
-   输出：**多尺度** 的体素特征，可用于下游的分割或检测任务 。

![Swin3D 整体网络架构图](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/2025%5C12%5Cimage-20251206140819429.png)

### Voxelization

体素化模块，论文中使用稀疏体素来表示点，如图 1 所示，根据输入点云，创建了 5 个不同层级的稀疏化体素网格，默认情况下，对于室内场景，划分最细的网格是 2cm，然后每提高一级，网格尺寸增加一倍；

点信息以从最精细的级别到最粗略级别的如下方式存储在体素中

-   对于最精细的体素网格 $v$，论文从这个体素网格中随机挑选一个点代表这个体素，记为 $r_v$；
-   后续层级（l+1）中，后续层级体素都比最精细的体素网格要大，一个体素相当于之前四个体素，这时从子体素的代表点中选择最接近几何中心的点；
-   这一步将无序的点云转化为结构化的稀疏体素，同时保留了点的原始信号 $s_v$ 。

### Initial Feature Embedding

论文中提到，参考 [Stratified transformer for 3D point cloud segmentation](https://arxiv.org/abs/2203.14508).发现的，直接使用线性层或 MLP 将原始特征投影到高维空间对于 Swin 系列的 transformer 架构无法产生比较好的效果，因此论文中提出使用一个 `3*3*3` 的卷积核对输入数据进行稀疏卷积（通过哈希表存储非空体素索引，避免大量空体素的无效计算），以及 BN 批量归一化和 ReLU 激活层，将输入体素特征变换到 $\mathbb{R}^{C_1}$

输入特征由体素 $v$ 的代表点坐标和体素中心坐标之差（$r_v-c_v$）和其他代表点特征（如 RGB、法向量等），相较于 [Stratified transformer for 3D point cloud segmentation](https://arxiv.org/abs/2203.14508) 中使用的 KPConv，论文中提出的 initial feature embedding 更轻量；

整理如下：

-   **输入**：体素 $v$ 的原始特征。这里的输入特征是由“位置偏移量”（$r_v - c_v$，即代表点坐标减去体素中心坐标）和其他信号（如颜色）拼接而成。
-   **操作**：使用一层 $3 \times 3 \times 3$ 的 **稀疏卷积 (Sparse Convolution)**，通过 Batch Normalization (BN) 和 ReLU 激活函数。
-   **目的**：将低维的原始信号投影到高维特征空间 $\mathbb{R}^{C_1}$。

### Contextual relative signal encoding（cRSE）

上下文相对信号编码，本质是对 Swin Transformer 中的相对位置编码的一种广义化增强

#### 1、为什么要有 cRSE？

在标准的 2D Swin Transformer 中，像素是排列在规则网格上的，相对位置是固定的。但在 3D 点云中，Swin3D 面临两个特殊挑战：

1.  **位置不规则 (Spatial Irregularity)**：点在体素内可以是任意位置，不仅仅是网格中心 1。
2.  **信号不规则 (Signal Irregularity)**：除了位置，点云还包含颜色（RGB）、法向量（Normal）等信号。在一个窗口内，这些信号的相对变化（例如两个点颜色差异很大）对于理解场景非常重要 2222。

原理解释：传统的相对位置编码只告诉注意力机制：“点 A 和点 B 在空间上距离是多少”。cRSE (Contextual Relative Signal Encoding) 则试图告诉注意力机制：“点 A 和点 B 不仅空间距离是 $X$，而且它们的颜色差异是 $Y$，法向量差异是 $Z$。”

这种编码被称为“Contextual（上下文的）”，是因为它不仅仅加一个静态的偏置值，而是让这个偏置值与当前的 Query 和 Key 进行交互，使得注意力机制能动态地根据信号差异来调整关注度 。

#### 2. 计算过程：cRSE 是如何运作的？

cRSE 的计算过程可以分为三个步骤：**信号差分**、**量化与查表**、**融入注意力机制**。

##### 第一步：计算信号差异 ($\Delta s_{ij}$)

对于窗口内的任意两个体素 $i$ 和 $j$，首先计算它们原始信号的差异。
$$
\Delta s_{ij} = s_{v_i} - s_{v_j}
$$
这里的信号 $s$ 是一个复合向量，通常包含：

-   **位置**：$x, y, z$
-   **颜色**：$r, g, b$
-   法向量：$n_x, n_y, n_z$，这意味着 cRSE 不仅编码位置差，也编码颜色差和法向量差。

##### 第二步：量化与查表 (Quantization & Look-up Table)

由于 $\Delta s_{ij}$ 是连续的浮点数，无法直接作为索引去查找参数。因此需要将其 **量化** 为整数索引，然后去一个可学习的 **查找表 (Look-up Table, LUT)** 中取值。

1.  量化公式 ：对于信号的第 $l$ 个分量（例如红色分量 R），计算索引 $I_l$：
    $$
    I_l(\Delta) = \left\lfloor \frac{(\Delta [l] - \text{min\_val}) \times L}{\text{range}} \right\rfloor
    $$

    -   $\text{min\_val}$ 和 $\text{range}$ 是预定义的范围（例如 RGB 颜色范围是 $[-1, 1]$）6。
    -   $L$ 是表的大小（例如颜色和法向量设为 16，位置设为 4）7。

2.  查表映射 ：通过索引 $I_l$，从可学习的表 $t^Q, t^K, t^V$ 中取出对应的向量。
    $$
    t_{Q, h}(\Delta) = \sum_{l = 1}^{m} t_{l, h}^Q [I_l(\Delta)]
    $$
    这意味着将位置差、颜色差、法向量差对应的特征向量相加，得到一个综合的信号差异编码。

##### 第三步：融入注意力计算 (Integration)

这是最关键的一步。cRSE 不仅仅是给 Attention Score 加一个标量 $b$，它是将信号差异编码投影后，分别与 Query 和 Key 进行交互。

1.   修改 Attention Score ($e_{ij}$)，原始 Attention 是 $(Q \cdot K^T) / \sqrt{d}$。加入 cRSE 后，公式变为：

$$
e_{ij, h} = \frac{(f_i W_{Q, h})(f_j W_{K, h})^T + b_{ij, h}}{\sqrt{d}}
$$

其中 $b_{ij,h}$ 是上下文偏差项：
$$
b_{ij, h} = \underbrace{(f_i W_{Q, h}) \cdot t_{Q, h}(\Delta s_{ij})}_{\text{Query 与信号差的交互}} + \underbrace{(f_j W_{K, h}) \cdot t_{K, h}(\Delta s_{ij})}_{\text{Key 与信号差的交互}}
$$

-   **直观理解**：这使得注意力分数不仅取决于 $Q$ 和 $K$ 的相似度，还取决于 $Q$ 对“信号差异”的敏感度以及 $K$ 对“信号差异”的敏感度。
-   修改 Output Value ($f^*$)

cRSE 不仅影响权重的计算，还直接把信号差异信息加到了 Value ($V$) 上 10：
$$
f_{i, h}^* = \frac{\sum_{j} \exp(e_{ij, h}) (f_j W_{V, h} + t_{V, h}(\Delta s_{ij}))}{\sum_{j} \exp(e_{ij, h})}
$$


-   这里 $t_{V,h}(\Delta s_{ij})$ 被直接加到了 $V$ 特征上。这意味着如果两个点的颜色差异很大，这个差异本身也会被作为特征传递到下一层。

### 总结

**cRSE 的本质** 是将 **[位置差, 颜色差, 法向量差]** 这一物理世界的先验知识，通过 **量化查表** 的方式变成可学习的向量，并强行注入到 Transformer 的 **Query-Key 匹配过程** 以及 **Value 聚合过程** 中。

这使得 Swin3D 能够理解：“虽然这个点在空间上很近，但颜色完全不同（可能是边界），所以我应该减少对它的注意力（降低 $e_{ij}$）”。

### W-MSA3D and SW-MSA3D

Swin3D 中的 Transformer Block，S-MSA3D 用于规则窗口，SW-MSA3D 用于偏移窗口，

S-MSA3D (规则窗口)：

-   切分方式：规则窗口从从坐标原点 $(0,0,0)$ 开始，按照固定的窗口大小 $M \times M \times M$ 把整个点云体素网格切成整齐的小方块 ；
-   局限性：自注意力计算被限制在每个 $M \times M \times M$ 的小方块内部。**不同方块之间的体素无法进行交互**。如果没有后续步骤，整个网络就会变成一个个孤立的“孤岛”，丢失全局信息。

SW-MSA3D (移位窗口)

-   **切分方式**：在 S-MSA3D 的基础上，将切分网格向右、下、后方移动。
-   **移动偏移量**：偏移量通常是窗口大小的一半，即 $(\lfloor \frac{M}{2} \rfloor, \lfloor \frac{M}{2} \rfloor, \lfloor \frac{M}{2} \rfloor)$ 6。
-   **目的**：**打破“孤岛”**。通过移动窗口，原来的边界变成了新窗口的中心。这样，原本在 S-MSA3D 中属于两个不同窗口的相邻体素，在 SW-MSA3D 中就会被包含在同一个窗口内进行交互。

### Downsample

$l$ 层的体素如何通过下采样变成 $l+1$ 层的体素呢？$l+1$ 层是在原始点云中采用 $l$ 层双倍的网格大小划分的体素，$l$ 层体素中每个体素的特诊表示经过 `LayerNorm+Linear Layer`，将特征维度从 $C_l$ 提升到 $C_{l+1}$，这是在 l 层的体素数量是操作的；然后是 KNNPooling，这是针对稀疏数据的特殊池化。对于下一层（$l+1$ 层）的每个体素，在上一层（$l$ 层）中找到其 **K 个最近邻 (K-Nearest Neighbors)** 体素，然后执行 **最大池化 (Max Pooling)** 21。默认 $k=16$。











































































































，借鉴



