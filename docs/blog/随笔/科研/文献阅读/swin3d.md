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



## 在pointcept中复现教程

### 1、创建自己的数据集读取器

在`pointcept/datasets`下新建一个`keypoint_dataset.py`，在里面创建一个pytorch风格的数据加载器，具体代码如下：

```python
import os
import glob
from typing import Any
from typing import Any
from typing import Any
from typing import Any
import numpy as np
import torch
from torch.utils.data import Dataset
from .builder import DATASETS
from .transform import Compose, TRANSFORMS

@DATASETS.register_module()
class KeypointDataset(Dataset):
    def __init__(self,
                 split='train',
                 data_root='data',
                 transform=None,
                 test_mode=False,
                 loop=1):
        super().__init__()
        self.data_root = data_root
        self.split = split
        # 加载转换流水线 (GridSample, ToTensor 等)
        self.transform = Compose(transform)
        self.test_mode = test_mode
        self.loop = loop if not test_mode else 1
        
        # 扫描文件
        self.data_list = self._get_file_list()
        print(f"[{self.split}] Loaded {len(self.data_list)} samples from {self.data_root}")

    def _get_file_list(self):
        split_path = os.path.join(self.data_root, self.split)
        if not os.path.exists(split_path):
            raise ValueError(f"Data path does not exist: {split_path}")

        # 匹配特征文件: *d_pc_clipped.npy
        feature_files = glob.glob(os.path.join(split_path, "*_d_pc_clipped.npy"))
        data_list = []

        for feat_path in feature_files:
            filename = os.path.basename(feat_path)
            # 解析文件名: dev_2_005J_20251102_110034_430_d_pc_clipped.npy
            # parts: ['dev', '2', '005J', '20251102', '110034', '430', ...]
            parts = filename.split('_')
            
            # 提取时间戳 (根据你的示例是第3,4,5个部分)
            # 请根据实际文件名调整这里的索引
            try:
                timestamp = f"{parts[3]}_{parts[4]}_{parts[5]}"
            except IndexError:
                print(f"Skipping invalid filename: {filename}")
                continue
            
            label_filename = f"关键点坐标_{timestamp}.npy"
            label_path = os.path.join(split_path, label_filename)

            if os.path.exists(label_path):
                data_list.append({
                    "feat_path": feat_path,
                    "label_path": label_path,
                    "name": filename
                })
        
        return data_list

    def __len__(self):
        return len(self.data_list) * self.loop

    def __getitem__(self, idx):
        idx = idx % len(self.data_list)
        info = self.data_list[idx]
        
        # 1. 加载数据
        raw_data = np.load(info["feat_path"]).astype(np.float32)
        coord = raw_data[:, 0:3]
        feat = raw_data[:, 3:]
        target = np.load(info["label_path"]).astype(np.float32)

        # 提取给 Swin3D 做位置编码辅助的特征 (coord_feat)
        # Swin3D 需要这个键。既然没有 RGB，就用 "法向量" (第3,4,5列) 代替
        # 维度: (N, 3)
        coord_feat = raw_data[:, 3:6]

        # ================= [新增] 数据安全检查 =================
        # 检查是否有 NaN 或 Inf
        if np.isnan(coord).any() or np.isinf(coord).any():
            print(f"⚠️ Warning: Found NaN/Inf in {info['name']}, replacing with 0.")
            coord = np.nan_to_num(coord) # 将 NaN 替换为 0
            
        if np.isnan(target).any() or np.isinf(target).any():
            print(f"⚠️ Warning: Found NaN/Inf in target of {info['name']}, replacing with 0.")
            target = np.nan_to_num(target)
        # =====================================================
        
        # 2. 去中心化
        centroid = np.mean(coord, axis=0)
        coord -= centroid
        target -= centroid

        # 3. 归一化
        # 增加 eps 防止除以 0 的隐患
        dist = np.sqrt(np.sum(coord ** 2, axis=1))
        m = np.max(dist) if dist.shape[0] > 0 else 0
        
        if m < 1e-6:
            m = 1.0
        
        m = float(m) 
        # coord = coord / m  <-- 原代码
        # target = target / m <-- 原代码
        
        # [修改建议] 防止 m 为 0 (虽然你前面处理了，但双重保险更好)
        scale = np.array(m, dtype=np.float32) 
        
        coord = coord / scale
        target = target / scale

        # 构造数据字典
        data_dict = dict(
            coord=coord,
            feat=feat,
            target=target, 
            coord_feat=coord_feat,  # [新增] Swin3D 位置编码辅助特征
            name=info["name"],
            centroid=centroid, 
            scale=scale  # [重点] 这里传入 numpy 数组，方便 DataLoader 自动堆叠
        )

        # 4. 应用变换 (GridSample 等)
        if self.transform is not None:
            data_dict = self.transform(data_dict)
            
        return data_dict


```

主要作用是从数据集路径下读取数据集，根据时间戳来匹配样本特征和标签，并进行预处理，包括去中心化、归一化，以及根据模型架构特点，是否进行网格化还是下采样等等，然后由统一的数据生成器打包为batch，供后面使用。

然后在同级目录下的`__init__.py`中注册我们自己创建的自己的数据集加载类，在文件末尾添加一行：

```python
# keypoint
from .keypoint_dataset import KeypointDataset
```



### 2、创建模型配置文件

在`configs`下新建一个文件夹`my_dataset`，然后新建一个`keypoint_swin3d.py`，`pointcept`中通过py文件配置模型参数，包括训练结果、日志等的保存路径，模型网络结构超参数，数据集路径，数据预处理方式，以及优化器、学习率调度器、钩子函数等等；

`keypoint_swin3d.py`文件内容如下：

```python
_base_ = ["../_base_/default_runtime.py"]

# ==============================================================================
# Global Settings
# ==============================================================================
epoch = 100 
save_path = "exp/keypoint_swin3d"
# ==============================================================================
# Model Settings (Swin3D)
# ==============================================================================
model = dict(
    type="KeypointSwin3D",
    num_keypoints=6,
    backbone_conf=dict(
        type="Swin3D-v1m1",
        in_channels=4, # 或 4，取决于你的 coord_feat 逻辑
        num_classes=64,
        
        base_grid_size=0.02,
        quant_size=50,       # 必须是整数
        num_layers=4,        # 必须显式指定为 4
        
        depths=[2, 2, 6, 2],
        channels=[64, 128, 256, 512],
        
        # [核心修改] 必须全为偶数！
        # 原来是 [3, 6, 12, 24] -> 改为 [6, 12, 24, 48] 或者 [4, 8, 16, 32]
        num_heads=[4, 8, 16, 32], 
        
        window_sizes=[5, 7, 7, 7],
        up_k=3,
        drop_path_rate=0.2,
        stem_transformer=True,
        down_stride=2,
        upsample="linear",
        knn_down=True,
        cRSE="XYZ_RGB",
        fp16_mode=1, 
    ),

    hidden_dim=256,
)

# ==============================================================================
# Data Settings
# ==============================================================================
num_worker = 4
batch_size = 8
data_root = "/home/gzh/point/DataSets"
grid_size_val = 0.02 # 这里的 grid_size 必须与模型的 quant_size/base_grid_size 匹配

data = dict(
    train=dict(
        type="KeypointDataset",
        split="train",
        data_root=data_root,
        transform=[
            dict(type="Update", keys_dict=dict(index_valid_keys=["coord", "feat", "coord_feat"], grid_size=grid_size_val)),
            dict(type="GridSample", grid_size=grid_size_val, hash_type="fnv", mode="train", return_grid_coord=True),
            dict(type="ToTensor"),
            dict(type="Collect", 
                 keys=("coord", "grid_coord", "feat", "target","coord_feat", "grid_size", "scale"), 
                 offset_keys_dict=dict(offset="coord"), 
                 feat_keys=("feat",),
                 coord_feat_keys=("coord_feat",))
        ],
        loop=1,
    ),
    val=dict(
        type="KeypointDataset",
        split="val",
        data_root=data_root,
        transform=[
            dict(type="Update", keys_dict=dict(index_valid_keys=["coord", "feat", "coord_feat"], grid_size=grid_size_val)),
            dict(type="GridSample", grid_size=grid_size_val, hash_type="fnv", mode="train", return_grid_coord=True),
            dict(type="ToTensor"),
            dict(type="Collect", 
                 keys=("coord", "grid_coord", "feat", "target", "coord_feat", "grid_size", "scale"), 
                 offset_keys_dict=dict(offset="coord"), 
                 feat_keys=("feat",),
                 coord_feat_keys=("coord_feat",))
        ],
    ),
    test=dict(
        type="KeypointDataset",
        split="test",
        data_root=data_root,
        transform=[
            dict(type="Update", keys_dict=dict(index_valid_keys=["coord", "feat", "coord_feat"], grid_size=grid_size_val)),
            dict(type="GridSample", grid_size=grid_size_val, hash_type="fnv", mode="train", return_grid_coord=True),
            dict(type="ToTensor"),
            dict(type="Collect", 
                 keys=("coord", "grid_coord", "feat", "target", "coord_feat", "grid_size", "scale"), 
                 offset_keys_dict=dict(offset="coord"), 
                 feat_keys=("feat",),
                 coord_feat_keys=("coord_feat",))
        ],
    ),
)

# ==============================================================================
# Training Settings
# ==============================================================================
optimizer = dict(type="AdamW", lr=0.002, weight_decay=0.05)
scheduler = dict(type="CosineAnnealingLR", eta_min=1e-5) 

hooks = [
    dict(type="CheckpointLoader"),
    dict(type="IterationTimer", warmup_iter=10),
    dict(type="InformationWriter"),
    dict(type="KeypointEvaluator"),
    dict(type="CheckpointSaver", save_freq=20)
]

```

### 3、创建具体网络模型结构

由于`pointcept`中现有的网络结构基本都是基于点云分类和点云的语义分割的，没有直接可用于点云关键点预测或者回归的，所以我们需要仿照`pointcept/models`路径下，已有的各种模型的网络结构，来修改分类头或者分割头，改为我们的关键点回归头；对于`swin3d`而言，我们在`pointcept/models`文件夹下创建我们的基于`swin3d`的关键点回归头的网络结构文件`keypoint_swin3d.py`，具体代码如下：

```python
# ==============================================================================
# pointcept/models/keypoint_swin3d.py
# 代码作用：Swin3D 关键点检测模型架构 
# ==============================================================================

import torch
import torch.nn as nn
from pointcept.models.builder import MODELS, build_model

@MODELS.register_module("KeypointSwin3D")
class KeypointSwin3D(nn.Module):
    def __init__(self, 
                 backbone_conf, 
                 num_keypoints=6, 
                 hidden_dim=256):
        super().__init__()
        # 1. 构建骨干网络 (Swin3D)
        self.backbone = build_model(backbone_conf)
        
        # 2. 自动获取骨干输出通道数
        # Swin3D 的 channels 参数通常是一个列表 [C1, C2, C3, C4]
        if 'channels' in backbone_conf:
            in_channels = backbone_conf['channels'][0]
        else:
            in_channels = 96 # 默认备用值

        # 3. 回归头 (Regression Head)
        self.num_keypoints = num_keypoints
        output_dim = num_keypoints * 3
        
        self.reg_head = nn.Sequential(
            nn.Linear(in_channels, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(inplace=True),
            nn.Linear(hidden_dim, output_dim)
        )
        
        # 4. 损失函数
        self.criterion = nn.MSELoss()

    def forward(self, data_dict):
        # === [核心修复] 构造 Swin3D 必须的 coord_feat ===
        if "coord_feat" not in data_dict:
            coord = data_dict["coord"]
            feat = data_dict["feat"]
            
            # 获取 Stem Layer (第一层卷积) 期望的输入通道数
            # 修正：根据 mink_layers.py，MinkConvBNRelu 使用 conv_layers (Sequential)
            try:
                stem = self.backbone.stem_layer
                if hasattr(stem, "conv_layers"): 
                    # 访问 Sequential 的第一个模块 (MinkowskiConvolution)
                    expected_channels = stem.conv_layers[0].in_channels
                elif hasattr(stem, "conv"):
                    expected_channels = stem.conv.in_channels
                else:
                    # 如果无法推断，默认使用配置中的 feat 维度
                    expected_channels = feat.shape[1]
            except Exception:
                expected_channels = feat.shape[1]

            # 根据模型期望决定是否拼接坐标
            if expected_channels == feat.shape[1] + 3:
                data_dict["coord_feat"] = torch.cat([coord, feat], dim=1)
            else:
                # 默认只使用特征 (如果是 4 通道)
                data_dict["coord_feat"] = feat

        # === 1. 特征提取 (Backbone) ===
        output = self.backbone(data_dict)
        
        # 兼容性处理：Swin3D 可能直接返回 Tensor，也可能返回 SparseTensor
        if hasattr(output, "F"): 
            feat = output.F
        else: 
            feat = output

        # === 2. 全局池化 (Global Pooling) ===
        # 使用 offset 将 batch 中每个样本的点特征聚合
        offset = data_dict["offset"].int()
        batch_feats = []
        start = 0
        
        # 注意：如果 Swin3D 使用了体素化导致点数变化，必须使用 offset2batch 等方式重新计算
        # 但 Pointcept 的 Swin3DUNet 在分割模式下通常会插值回原始点数，或者保持一一对应
        # 为了安全，这里做一个长度检查
        if feat.shape[0] != offset[-1].item():
            # 如果特征点数与原始 offset 不一致 (说明被体素化下采样了)
            # 我们需要重新计算一个 batch 索引
            batch_idx = data_dict.get("batch", None)
            if batch_idx is None:
                # 如果没有 batch 索引，尝试用 coordinates 推断 (SparseTensor 的 coordinates 第一列是 batch_idx)
                if hasattr(output, "C"):
                    batch_idx = output.C[:, 0]
                else:
                    raise RuntimeError("Output feature size mismatch and cannot infer batch index.")
            
            # 使用 scatter_mean 或简单的循环进行池化
            for b in range(len(offset)):
                mask = (batch_idx == b)
                if mask.any():
                    sample_feat = feat[mask].mean(dim=0)
                else:
                    sample_feat = torch.zeros_like(feat[0])
                batch_feats.append(sample_feat)
        else:
            # 正常情况：点数一一对应
            for i in range(len(offset)):
                end = offset[i]
                sample_feat = feat[start:end].mean(dim=0) 
                batch_feats.append(sample_feat)
                start = end
        
        global_feat = torch.stack(batch_feats, dim=0) # (B, C)

        # === 3. 关键点回归 ===
        pred_flat = self.reg_head(global_feat)
        pred = pred_flat.view(-1, self.num_keypoints, 3)

        result_dict = {}

        # === 4. Loss 与 监控 ===
        if "target" in data_dict:
            target = data_dict["target"]
            
            pred_for_loss = pred if pred.shape == target.shape else pred.view(-1, 3)
            loss = self.criterion(pred_for_loss, target)
            if loss.ndim > 0: loss = loss.mean()
            result_dict["loss"] = loss

            if self.training:
                with torch.no_grad():
                    k = self.num_keypoints
                    pred_metric = pred.view(-1, k, 3)
                    target_metric = target.view(-1, k, 3)

                    dist = torch.norm(pred_metric - target_metric, p=2, dim=-1)

                    if "scale" in data_dict:
                        scale = data_dict["scale"]
                        if scale.ndim == 1: scale = scale.view(-1, 1)
                        dist = dist * scale
                    
                    result_dict["train/mean_dist"] = dist.mean()
                    
                    kp_dist_mean = dist.mean(dim=0)
                    for i in range(k):
                        result_dict[f"train/kp{i}_dist"] = kp_dist_mean[i]

        if self.training:
            return result_dict
        else:
            result_dict["pred"] = pred
            return result_dict
```

对于`swin3d`而言，我们只使用`stage5`，也就是最后一个阶段输出的**最高层（语义最强、分辨率最低）**的特征，然后在体素数量维度N上进行平均池化，得到通道为$C_5$的特征向量，然后通过回归头（一个简单的3层MLP）将特征映射到`number_points*3`维度上，然后使用真实关键点坐标优化这个输出，得到我们想要的关键点坐标。

创建好`pointcept/models/keypoint_swin3d.py`文件后，和数据集配置文件类似，在`pointcept/models/__init__.py`中注册我们创建的模型网络架构，具体来说，在文件末尾添加一行，导入我们创建的模型网络架构类

```python
from .keypoint_swin3d import KeypointSwin3D     # 基于Swin3D的关键点检测模型
```

### 4、训练模型

在tools/train.py中，分别运行如下代码：

```cmd
export PYTHONPATH=.
source .venv/bin/activate
python tools/train.py --config-file configs/my_dataset/keypoint_swin3d.py
```

即可开始训练

### 5、推理

新建`tools/inference.py`，代码如下：实现了trian、val、test的单独批量评估，并绘制关键点误差散点图。以及单样本推理并使用open3d绘制关键点可视化

```python
"""
Keypoint Detection Inference & Visualization Script
功能：
1. 支持单样本推理：计算误差 + Open3D 可视化（球体=真值，立方体=预测）
2. 支持批量推理：计算整个数据集的平均误差 (Mean) 和标准差 (Std)
3. 架构通用：通过 config 文件自动加载对应的模型架构
"""

import argparse
import os
import sys
import numpy as np
import torch
import open3d as o3d
import matplotlib.pyplot as plt
from tqdm import tqdm

# 添加项目根目录到 python path，确保能导入 pointcept
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from pointcept.utils.config import Config, DictAction
from pointcept.models import build_model
from pointcept.datasets import build_dataset, point_collate_fn
from pointcept.utils.misc import intersection_and_union, make_dirs
from pointcept.engines.defaults import default_argument_parser

def get_args():
    parser = argparse.ArgumentParser(description="Pointcept Keypoint Inference")
    parser.add_argument("--config-file", default="configs/my_dataset/keypoint_ptv3.py", help="配置文件路径")
    parser.add_argument("--options", nargs="+", action=DictAction, help="覆盖配置文件的参数")
    parser.add_argument("--weights", default=None, required=True, help="模型权重文件路径 (.pth)")
    parser.add_argument("--subset", default="val", choices=["train", "val", "test"], help="数据集划分")
    parser.add_argument("--idx", type=int, default=-1, help="单样本索引。如果为 -1，则进行批量推理")
    
    # 可视化参数
    parser.add_argument("--visualize", action="store_true", help="是否开启 Open3D 可视化 (仅单样本模式有效)")
    parser.add_argument("--sphere-radius", type=float, default=0.05, help="真实关键点(球)的半径")
    parser.add_argument("--cube-size", type=float, default=0.08, help="预测关键点(正方体)的边长")
    parser.add_argument("--point-size", type=float, default=2.0, help="Open3D 可视化时点云的点大小")
    parser.add_argument("--save-dir", default=None, help="结果保存路径 (可选)")
    
    args = parser.parse_args()
    return args

def setup_model(cfg, weights_path):
    """加载模型和权重"""
    print(f"=> Building model from config: {cfg.model.type}")
    model = build_model(cfg.model)
    
    if os.path.isfile(weights_path):
        print(f"=> Loading weights from {weights_path}")
        checkpoint = torch.load(weights_path, map_location="cuda")
        state_dict = checkpoint.get("state_dict", checkpoint)
        # 移除 'module.' 前缀 (如果是 DDP 训练保存的)
        new_state_dict = {k.replace("module.", ""): v for k, v in state_dict.items()}
        model.load_state_dict(new_state_dict, strict=True)
    else:
        raise FileNotFoundError(f"No weights found at {weights_path}")
    
    model.cuda()
    model.eval()
    return model

def create_colored_mesh(geometry_type, center, color, size):
    """创建带颜色的几何体 (球或立方体)"""
    if geometry_type == 'sphere':
        mesh = o3d.geometry.TriangleMesh.create_sphere(radius=size)
    elif geometry_type == 'box':
        mesh = o3d.geometry.TriangleMesh.create_box(width=size, height=size, depth=size)
        # Box 默认原点在角落，需要平移到中心
        mesh.translate(-np.array([size/2, size/2, size/2]))
    
    mesh.translate(center)
    mesh.paint_uniform_color(color)
    return mesh

def visualize_single(coord, pred_kps, target_kps, args, num_kps):
    """使用 Open3D 可视化 (支持调整点大小)"""
    print(f"=> Visualizing... (Point Size: {args.point_size})")
    geometries = []

    # 1. 点云 (灰色)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(coord)
    pcd.paint_uniform_color([0.7, 0.7, 0.7]) # 灰色点云
    geometries.append(pcd)

    # 2. 关键点颜色映射
    cmap = plt.get_cmap("jet")
    colors = [cmap(i / (num_kps - 1 if num_kps > 1 else 1))[:3] for i in range(num_kps)]

    # 3. 绘制关键点
    for i in range(num_kps):
        # 真实值：圆球 (Sphere)
        if target_kps is not None:
            sphere = create_colored_mesh('sphere', target_kps[i], colors[i], args.sphere_radius)
            geometries.append(sphere)
        
        # 预测值：正方体 (Cube)
        cube = create_colored_mesh('box', pred_kps[i], colors[i], args.cube_size)
        geometries.append(cube)

    # 4. [修改核心] 使用 Visualizer 来控制渲染选项
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name=f"Sample {args.idx} (Sphere=GT, Cube=Pred)", width=1024, height=768)
    
    # 添加所有几何体
    for geom in geometries:
        vis.add_geometry(geom)
        
    # 获取并修改渲染选项
    opt = vis.get_render_option()
    opt.point_size = args.point_size        # [关键] 设置点的大小
    opt.background_color = np.asarray([1, 1, 1]) # [可选] 设置背景为白色，看起来更清晰
    
    vis.run()
    vis.destroy_window()


def inference_single_sample(cfg, model, dataset, args):
    """单样本推理逻辑"""
    idx = args.idx
    if idx >= len(dataset):
        print(f"Error: Index {idx} out of bounds (Dataset size: {len(dataset)})")
        return

    # 1. 获取数据
    data_dict = dataset[idx]
    # Collate: 即使是单个样本，也需要伪造成 batch 为 1 的形式 (增加 batch 维度)
    data_dict = point_collate_fn([data_dict])
    
    # 转移到 GPU
    for key in data_dict:
        if isinstance(data_dict[key], torch.Tensor):
            data_dict[key] = data_dict[key].cuda(non_blocking=True)

    # 2. 推理
    with torch.no_grad():
        result = model(data_dict)
        # 兼容不同的返回格式 (有的模型返回字典，有的返回 Tensor)
        pred = result["pred"] if isinstance(result, dict) else result

    # 3. 数据后处理 (GPU -> CPU -> Numpy)
    # pred shape: (1, K, 3) -> (K, 3)
    # target shape: (1, K, 3) -> (K, 3)
    num_kps = cfg.model.num_keypoints
    pred = pred.view(-1, num_kps, 3).cpu().numpy()[0]
    
    target = None
    if "target" in data_dict:
        target = data_dict["target"].view(-1, num_kps, 3).cpu().numpy()[0]

    # 获取点云坐标用于可视化 (优先用原始 coord，如果没有则用 grid_coord * grid_size)
    coord = data_dict["coord"].cpu().numpy()
    
    # 4. 计算误差 (逆归一化)
    scale = 1.0
    if "scale" in data_dict:
        scale = data_dict["scale"].cpu().numpy()[0] # (1,) -> scalar
    elif "grid_size" in data_dict:
        # 如果没有 scale 只有 grid_size，且 target 是体素坐标，则用 grid_size
        scale = data_dict["grid_size"]
        if isinstance(scale, torch.Tensor): scale = scale.item()

    print(f"\n====== Inference Result [Sample IDX: {idx}] ======")
    print(f"Scale Factor: {scale}")

    if target is not None:
        # 计算欧氏距离
        # 注意：pred 和 target 目前通常是在归一化坐标系下
        diff = np.linalg.norm(pred - target, axis=-1) # (K,)
        
        # 逆归一化到原始物理尺度
        real_diff = diff * scale 

        print("-" * 40)
        print(f"{'Keypoint ID':<15} | {'Error (Original Scale)':<25}")
        print("-" * 40)
        for i in range(num_kps):
            print(f"KP {i:<12} | {real_diff[i]:.4f}")
        print("-" * 40)
        print(f"Mean Error      | {np.mean(real_diff):.4f}")
        print("-" * 40)
    
    # 5. 可视化
    if args.visualize:
        # 坐标通常也需要缩放以便可视化正确（如果 coord 也是归一化的）
        # 这里我们直接画归一化空间下的，或者全部乘 scale
        # 为了方便观察相对位置，直接画归一化空间下的即可，只要 scale 一致
        visualize_single(coord, pred, target, args, num_kps)


def plot_batch_errors(all_errors, num_kps):
    """
    绘制关键点误差散点图
    layout: 2行3列 (针对6个关键点)
    """
    import matplotlib.pyplot as plt
    
    # 设置绘图风格
    plt.style.use('ggplot')
    
    # 创建画布，2行3列
    rows, cols = 2, 3
    fig, axes = plt.subplots(rows, cols, figsize=(18, 10))
    fig.suptitle('Keypoint Prediction Errors (Batch Inference)', fontsize=16)
    
    # 展平 axes 方便索引
    axes = axes.flatten()
    
    # 样本序号 (X轴)
    x = np.arange(all_errors.shape[0])
    
    for i in range(num_kps):
        if i >= len(axes): break # 防止关键点数量超过子图数量
        
        ax = axes[i]
        y = all_errors[:, i] # 第 i 个关键点的所有样本误差
        
        # 统计指标
        mean_val = np.mean(y)
        std_val = np.std(y)
        upper_limit = mean_val + 2 * std_val
        
        # 1. 绘制散点
        ax.scatter(x, y, alpha=0.6, s=10, c='blue', label='Sample Error')
        
        # 2. 绘制平均值虚线 (红色)
        ax.axhline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.4f}')
        
        # 3. 绘制 2*标准差 虚线 (绿色)
        ax.axhline(upper_limit, color='green', linestyle='--', linewidth=2, label=f'Mean+2Std: {upper_limit:.4f}')
        
        # 标签设置
        ax.set_title(f'Keypoint {i}', fontsize=12)
        ax.set_xlabel('Sample Index')
        ax.set_ylabel('Error (m)')
        ax.legend(loc='upper right', fontsize=8)
        ax.grid(True, which='both', linestyle='--', alpha=0.7)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # 调整布局防止重叠
    plt.show() # 弹出窗口

def inference_batch(cfg, model, dataset, args):
    """批量推理逻辑"""
    print(f"=> Start Batch Inference on [{args.subset}] set...")
    dataloader = torch.utils.data.DataLoader(
        dataset, 
        batch_size=cfg.data.batch_size if hasattr(cfg.data, "batch_size") else 1,
        shuffle=False, 
        num_workers=cfg.num_worker, 
        collate_fn=point_collate_fn,
        pin_memory=True
    )

    num_kps = cfg.model.num_keypoints
    all_errors = [] # 存储所有样本所有关键点的误差

    model.eval()
    with torch.no_grad():
        for i, data_dict in enumerate(tqdm(dataloader)):
            # GPU
            for key in data_dict:
                if isinstance(data_dict[key], torch.Tensor):
                    data_dict[key] = data_dict[key].cuda(non_blocking=True)
            
            # Forward
            result = model(data_dict)
            pred = result["pred"] if isinstance(result, dict) else result
            
            target = data_dict["target"]
            
            # Reshape (B, K, 3)
            pred = pred.view(-1, num_kps, 3)
            target = target.view(-1, num_kps, 3)
            
            # Calc Distance in Normalized Space
            dist = torch.norm(pred - target, p=2, dim=-1) # (B, K)
            
            # Inverse Normalization
            if "scale" in data_dict:
                scale = data_dict["scale"] # (B,)
                if scale.ndim == 1: scale = scale.view(-1, 1)
                dist = dist * scale
            elif "grid_size" in data_dict:
                # Fallback logic
                g = data_dict["grid_size"]
                dist = dist * g

            all_errors.append(dist.cpu().numpy())

    # Concatenate all batches: (Total_Samples, K)
    all_errors = np.concatenate(all_errors, axis=0)
    
    # Statistics
    mean_per_kp = np.mean(all_errors, axis=0)
    std_per_kp = np.std(all_errors, axis=0)
    total_mean = np.mean(all_errors)

    print("\n====== Batch Inference Statistics ======")
    print(f"Total Samples: {all_errors.shape[0]}")
    print("-" * 65)
    print(f"{'Keypoint ID':<15} | {'Mean Error':<20} | {'Std Dev':<20}")
    print("-" * 65)
    for i in range(num_kps):
        print(f"KP {i:<12} | {mean_per_kp[i]:.5f}            | {std_per_kp[i]:.5f}")
    print("-" * 65)
    print(f"{'OVERALL':<15} | {total_mean:.5f}")
    print("-" * 65)

    # [新增] 调用绘图函数
    print("=> Plotting error distribution...")
    plot_batch_errors(all_errors, num_kps)

def main():
    args = get_args()
    
    # 1. 加载配置
    cfg = Config.fromfile(args.config_file)
    if args.options:
        cfg.merge_from_dict(args.options)
    
    # 2. 构建模型
    model = setup_model(cfg, args.weights)
    
    # 3. 构建数据集
    # 注意：只构建 args.subset 指定的那一部分 (train/val/test)
    if args.subset not in cfg.data:
        raise ValueError(f"Subset {args.subset} not found in config.data")
    
    dataset_cfg = cfg.data[args.subset]
    dataset_cfg.data_root = cfg.data_root # 确保 data_root 被正确传递
    dataset = build_dataset(dataset_cfg)
    
    print(f"=> Loaded {len(dataset)} samples from {args.subset} set.")

    # 4. 执行推理
    if args.idx != -1:
        # 单样本模式
        inference_single_sample(cfg, model, dataset, args)
    else:
        # 批量模式
        inference_batch(cfg, model, dataset, args)


"""
## 基于 Pointcept-PTv3 模型的推理脚本
python tools/inference.py \
    --config-file configs/my_dataset/keypoint_ptv3.py \
    --weights exp/keypoint_ptv3/model/model_best.pth \
    --subset test \
    --idx -1 \
    --visualize \
    --sphere-radius 0.02 \
    --cube-size 0.02
====== Batch Inference Statistics ======
Total Samples: 28
-----------------------------------------------------------------
Keypoint ID     | Mean Error           | Std Dev             
-----------------------------------------------------------------
KP 0            | 22.65371            | 13.36939
KP 1            | 21.20184            | 13.95168
KP 2            | 30.23071            | 20.58898
KP 3            | 27.92994            | 20.37176
KP 4            | 32.97409            | 18.85650
KP 5            | 34.39021            | 21.52718
-----------------------------------------------------------------
OVERALL         | 28.23009
-----------------------------------------------------------------



## 基于 Pointcept-OctFormer 模型的推理脚本
python tools/inference.py \
    --config-file configs/my_dataset/keypoint_octformer.py \
    --weights exp/keypoint_octformer/model/model_best.pth \
    --subset test \
    --idx -1 \
    --visualize \
    --sphere-radius 0.02 \
    --cube-size 0.02
====== Batch Inference Statistics ======
Total Samples: 28
-----------------------------------------------------------------
Keypoint ID     | Mean Error           | Std Dev             
-----------------------------------------------------------------
KP 0            | 33.27346            | 16.75899
KP 1            | 26.27490            | 15.12749
KP 2            | 31.13291            | 19.68741
KP 3            | 27.60023            | 18.44568
KP 4            | 32.59894            | 17.00893
KP 5            | 38.96297            | 19.05381
-----------------------------------------------------------------
OVERALL         | 31.64057
-----------------------------------------------------------------

## 基于 Pointcept-PTv1 模型的推理脚本
export PYTHONPATH=.
python tools/inference.py \
    --config-file configs/my_dataset/keypoint_ptv1.py \
    --weights exp/keypoint_ptv1/model/model_best.pth \
    --subset test \
    --idx -1 \
    --visualize \
    --sphere-radius 0.02 \
    --cube-size 0.02
====== Batch Inference Statistics ======
Total Samples: 28
-----------------------------------------------------------------
Keypoint ID     | Mean Error           | Std Dev             
-----------------------------------------------------------------
KP 0            | 26.13216            | 11.06119
KP 1            | 24.93169            | 17.54638
KP 2            | 31.74557            | 21.16514
KP 3            | 24.36304            | 16.39521
KP 4            | 22.96082            | 11.83866
KP 5            | 32.36544            | 11.43148
-----------------------------------------------------------------
OVERALL         | 27.08312
-----------------------------------------------------------------

## 基于 Pointcept-PTv2 模型的推理脚本
python tools/inference.py \
    --config-file configs/my_dataset/keypoint_ptv2.py \
    --weights exp/keypoint_ptv2/model/model_best.pth \
    --subset train \
    --idx -1 \
    --visualize \
    --sphere-radius 0.02 \
    --cube-size 0.02
====== Batch Inference Statistics ======
Total Samples: 28
-----------------------------------------------------------------
Keypoint ID     | Mean Error           | Std Dev             
-----------------------------------------------------------------
KP 0            | 27.17042            | 15.76558
KP 1            | 21.63920            | 18.46684
KP 2            | 30.25765            | 20.59952
KP 3            | 25.22526            | 18.56907
KP 4            | 25.64672            | 13.56527
KP 5            | 31.95988            | 13.46944
-----------------------------------------------------------------
OVERALL         | 26.98319
-----------------------------------------------------------------


## 基于 Swin3D 模型的推理脚本
python tools/inference.py \
    --config-file configs/my_dataset/keypoint_swin3d.py \
    --weights exp/keypoint_swin3d/model/model_best.pth \
    --subset test \
    --idx -1 \
    --visualize \
    --sphere-radius 0.02 \
    --cube-size 0.02
====== Batch Inference Statistics ======
Total Samples: 28
-----------------------------------------------------------------
Keypoint ID     | Mean Error           | Std Dev             
-----------------------------------------------------------------
KP 0            | 19.49621            | 11.82266
KP 1            | 21.12213            | 17.46186
KP 2            | 31.11461            | 21.69423
KP 3            | 25.54762            | 19.42591
KP 4            | 23.38527            | 13.12805
KP 5            | 25.49153            | 12.77503
-----------------------------------------------------------------
OVERALL         | 24.35956
-----------------------------------------------------------------
"""
if __name__ == "__main__":
    main()

```

例如，

```cmd
python tools/inference.py \
  --config-file configs/my_dataset/keypoint_swin3d.py \
  --weights exp/keypoint_swin3d/model/model_best.pth \
  --subset test \
  --idx 10 \
  --visualize \
  --sphere-radius 0.02 \
  --cube-size 0.02
```

运行效果如下：

```cmd
====== Inference Result [Sample IDX: 10] ======
Scale Factor: 873.6885986328125
----------------------------------------
Keypoint ID     | Error (Original Scale)   
----------------------------------------
KP 0            | 12.1654
KP 1            | 6.9847
KP 2            | 10.8451
KP 3            | 16.2290
KP 4            | 14.2673
KP 5            | 12.6374
----------------------------------------
Mean Error      | 12.1882
----------------------------------------
=> Visualizing... (Point Size: 2.0)
```

![image-20251214115708498](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/2025%5C12%5Cimage-20251214115708498.png)



























































































