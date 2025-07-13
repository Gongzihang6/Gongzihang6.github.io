---
title: 理解YOLO网络结构
author: gzh
img: 
top: 
top_img: 
cover: true
coverImg: /medias/featureimages/yolo.jpg
password: 
toc: true
aside: true
mathjax: true
summary: 按照backbone、neck、head介绍了yolov5的网络结构，并给出了代码和图示帮助理解
categories: deep learing
tags:
  - yolo
  - yolov5
date: 2023-04-06 23:18:00
---

### yolo网络结构详解



先来放上整个网络结构的示意图，图中所示为yolov5l的网络结构图

![yolov5l整体网络结构(部分参数不正确，以文中介绍为准)](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fyolov5.jpeg)

---

#### 一、Backbone结构

##### 1、Focus模块

​	进入backbone之前，对原始输入图像进行切片操作，每隔一个像素取一个值，图像高宽减半，通道数变为原来4倍，信息基本没有丢失，以yolov5s为例，输入图像640 *640 *3，经过Focus结构，变为  320 *320 *12，如图：640 *640 *3

![focus示意图](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2FFocus.png)

```python
# 展现在网络结构中就是先对输入图像进行切片操作，原始输入640* 640 *3，
# 切片后变为320* 320* 12
# 然后在经过两次卷积，640*640*3-->320*320*12-->320*320*64-->160*160*128
(0): Focus(
   (conv): Conv(
     (conv): Conv2d(12, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
      (act): SiLU(inplace=True)
      )
    )
(1): Conv(
   (conv): Conv2d(64, 128, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
    (act): SiLU(inplace=True)
    )
# 实现Focus模块的代码
class Focus(nn.Module):
    # Focus wh information into c-space
    def __init__(self, c1, c2, k=1, s=1, p=None, g=1, act=True):  # ch_in, ch_out, kernel, stride, padding, groups
        super(Focus, self).__init__()
        self.conv = Conv(c1 * 4, c2, k, s, p, g, act)
        # self.contract = Contract(gain=2)

    def forward(self, x):  # x(b,c,w,h) -> y(b,4c,w/2,h/2)
        # 对于4维张量x，...表示省略的维度，::2表示步长为2的切片。
        # 步长为2的切片后，在通道维度拼接起来，图像高宽减半，通道数变为原来4倍
        return self.conv(torch.cat([x[..., ::2, ::2], x[..., 1::2, ::2], x[..., ::2, 1::2], x[..., 1::2, 1::2]], 1))
        # return self.conv(self.contract(x))

```

##### 2、BottleNeck模块

下面两种BottleNeck模块分别用在模型的Backbone和neck部分，BottleNeck1用于Backbone，BottleNeck2用于neck，BottleNeck结构不改变图像高宽和通道数量。

![BottleNeck示意图](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2FBottleNeck.png)

由一个1* 1卷积和3* 3卷积，再加上残差连接组成

```python
class Bottleneck(nn.Module):
    # Standard bottleneck
    # 残差链接块，shortcut表示是否包含捷径路线,即BottleNeck1和即BottleNeck2
    # 由1*1卷积、3*3卷积和残差连接组成
    def __init__(self, c1, c2, shortcut=True, g=1, e=0.5):  # ch_in, ch_out, shortcut, groups, expansion
        super(Bottleneck, self).__init__()
        c_ = int(c2 * e)  # hidden channels
        self.cv1 = Conv(c1, c_, 1, 1)
        self.cv2 = Conv(c_, c2, 3, 1, g=g)
        self.add = shortcut and c1 == c2            # 确保残差连接shortcut前后的通道数一致，保证能够可以相加

    def forward(self, x):
        # 逐元素相加
        return x + self.cv2(self.cv1(x)) if self.add else self.cv2(self.cv1(x))				
### 输入为160*160*64时，输出为160*160*64
```

第一次进入BottleNeck1，图像形状为160* 160* 64，输出160* 160* 64



##### 3、C3模块

如图，C3模块由1* 1卷积和BottleNeck模块组成，构成了yolov5的核心组成部分。整体来说，C3模块先对输入图像做通道数减半的1*1卷积并分支，其中一个分支经过若干个BottleNeck, 然后两个分支在通道维concat，concat后得到的输出通道就和输入通道数一样了，最后再来一个通道数不变的

![C3模块示意图](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2FC3.png)

```python
class C3(nn.Module):
    # CSP Bottleneck with 3 convolutions
    def __init__(self, c1, c2, n=1, shortcut=True, g=1, e=0.5):  # ch_in, ch_out, number, shortcut, groups, expansion
        super(C3, self).__init__()
        c_ = int(c2 * e)  # hidden channels
        self.cv1 = Conv(c1, c_, 1, 1)
        self.cv2 = Conv(c1, c_, 1, 1)
        self.cv3 = Conv(2 * c_, c2, 1)  # act=FReLU(c2)
        self.m = nn.Sequential(*[Bottleneck(c_, c_, shortcut, g, e=1.0) for _ in range(n)])
        # self.m = nn.Sequential(*[CrossConv(c_, c_, 3, 1, g, 1.0, shortcut) for _ in range(n)])

    def forward(self, x):
        # 先对输入图像x进行cv1卷积，再来n个Bottleneck块，再和经过cv2卷积的输入图像x在通道维拼接，再经过cv3卷积
        return self.cv3(torch.cat((self.m(self.cv1(x)), self.cv2(x)), dim=1))
''''''
经过C3模块，图像由之前的160*160*128-->(cv1)160*160*64-->(3个BottleNeck)160*160*64
							  -->(cv2)160*160*64-->
    concat-->160*160*128-->(cv3)160*160*128
''''''
图像经过一个C3模块，大小和通道数都不发生改变
```

##### 4、后续网络走向

- 经过第一个C3模块，输出图像为160* 160* 128，然后一个卷积，变为80* 80* 256，此时得到的特征图称为P3

```python
    (3): Conv(
      (conv): Conv2d(128, 256, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
      (act): SiLU(inplace=True)
```

- 然后第二个C3模块，输入图像是80* 80* 256，输出图像也为80* 80* 256，然后一个卷积，变为40* 40* 512，此时得到的特征图称为P4

  ```
  # 第二个C3模块有9个BottleNeck
      (5): Conv(
        (conv): Conv2d(256, 512, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
        (act): SiLU(inplace=True)
  ```

- 然后第三个C3模块，输入图像是40* 40* 512，输出图像也是40* 40* 512，经过一个卷积，变为20* 20* 1024，此时得到的特征图称为P5

  ```python
  # 第三个C3模块有9个BOttleNeck
      (7): Conv(
        (conv): Conv2d(512, 1024, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
        (act): SiLU(inplace=True)
  ```

- 然后第四个C3模块（3个BottleNeck），输出图像是20* 20* 1024，输出图像也为20* 20* 1024，与之前不同的是这里并没有一个卷积使其图像高宽减半，通道数加倍，而是接一个**SPPF**模块



##### 5、**SPPF**

​		SSPF模块将经过CBS的x、一次池化后的y1、两次池化后的y2和3次池化后的self.m(y2)先进行拼接，然后再CBS提取特征。 仔细观察不难发现，虽然SSPF对特征图进行了多次池化，但是特征图尺寸并未发生变化，通道数更不会变化，所以后续的4个输出能够在channel维度进行融合。这一模块的主要作用是对高层特征进行提取并融合，在融合的过程中作者多次运用最大池化，尽可能多的去提取高层次的语义特征。

![SSPF示意图](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2FSSPF.jpg)

​		第三个C3模块结束后，进入SSPF模块，输入为20* 20* 1024，先经过一个卷积cv1， 变为20* 20* 512，然后顺序经过kernel_size为5、9、13的最大池化层并依次输出，图像大小和高宽均不发生变化，最后将这四个输出在通道维concat起来，四个20* 20 *512，拼接起来得到			20 * 20* 2048，然后经过cv2，变为20* 20* 1024

```
    (8): SPP(
      (cv1): Conv(
        (conv): Conv2d(1024, 512, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (cv2): Conv(
        (conv): Conv2d(2048, 1024, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (m): ModuleList(
        (0): MaxPool2d(kernel_size=5, stride=1, padding=2, dilation=1, ceil_mode=False)
        (1): MaxPool2d(kernel_size=9, stride=1, padding=4, dilation=1, ceil_mode=False)
        (2): MaxPool2d(kernel_size=13, stride=1, padding=6, dilation=1, ceil_mode=False)
      )
    )
```

​		至此，整个BackBone结构完毕，接下来分别是从第二个C3模块结束、第三个C3模块结束、SPPF模块结束引出的连接BackBone和Head(检测层)的Neck

#### 二、Neck结构

按照整体网络结构图中由下至上的顺序

##### 1、SPPF模块引出的neck

​		经过SPPF模块后，输出图像为20* 20* 1024，先经过一个卷积，通道数减半，变为20* 20* 512（记为**n1**,后面会用到），然后最近邻上采样，高宽加倍变为40* 40* 512，然后和第三个C3模块结束后的输出concat后变为40* 40* 1024，然后经过neck部分左下的C3模块，这里的C3会使输出通道数减半，高宽不变，输出40* 40* 512

```python
(10): Conv(
      (conv): Conv2d(1024, 512, kernel_size=(1, 1), stride=(1, 1))
      (act): SiLU(inplace=True)
    )
    (11): Upsample(scale_factor=2.0, mode='nearest')
    (12): Concat()
    (13): C3(
      (cv1): Conv(
        (conv): Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (cv2): Conv(
        (conv): Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (cv3): Conv(
        (conv): Conv2d(512, 512, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      # 这里BottleNeck中的卷积是256，图中有误
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
        (1): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
        (2): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
      )
    )
```

​		得到输出40* 40* 512后，经过一个卷积，通道数减半，得到40* 40* 256（记为**n2**), 然后一个最近邻上采样，得到80* 80* 256，然后和第二个C3模块引出的neck拼接在一起，得到80* 80* 512

```python
    (14): Conv(
      (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
      (act): SiLU(inplace=True)
    )
    (15): Upsample(scale_factor=2.0, mode='nearest')
    (16): Concat()
```

​		然后经过neck中左上角的C3模块，和左下角的C3模块一样，输出的图像高宽不变，通道数减半，关键是进入C3分支的两个卷积的输出通道都缩小了1/2（相比BackBone里的C3模块），输入为80* 80* 512，得到输出==80* 80* 256（记为**n3**)，同时也是**head1**, 进入检测层==

```python
    (17): C3(
      (cv1): Conv(
        (conv): Conv2d(512, 128, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (cv2): Conv(
        (conv): Conv2d(512, 128, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (cv3): Conv(
        (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
        (1): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
        (2): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
      )
    )
```

​		通过左上角的C3模块后，得到80* 80* 256的输出，然后进入一个卷积，通道数不变，高宽减半，输出为40* 40* 256，然后和**n2**的40* 40* 256concat，得到40* 40* 512，然后进入右上角的C3模块，右上角的C3模块和BackBone里的一样，不改变图像高宽和通道数，通过右上角的C3模块，得到输出为==40* 40* 512，也即**head2**，进入检测层==

```
(20): C3(
      (cv1): Conv(
        (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (cv2): Conv(
        (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (cv3): Conv(
        (conv): Conv2d(512, 512, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
        (1): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
        (2): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
      )
    )
```

​		通过右上角的C3模块后，输出为40* 40* 512，然后先经过一个卷积，使图像高宽减半、通道数不变，得到20* 20* 512，然后和**n1**的20* 20* 512concat得到20* 20* 1024，然后进入neck的右下角的C3模块，这个C3模块和BackBone里的一样，不改变图像高宽和通道数，通过C3模块后得到输出为==20* 20* 1024，也即**head3**，进入检测层==

```
    (21): Conv(
      (conv): Conv2d(512, 512, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
      (act): SiLU(inplace=True)
    )
    (22): Concat()
    (23): C3(
      (cv1): Conv(
        (conv): Conv2d(1024, 512, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (cv2): Conv(
        (conv): Conv2d(1024, 512, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (cv3): Conv(
        (conv): Conv2d(1024, 1024, kernel_size=(1, 1), stride=(1, 1))
        (act): SiLU(inplace=True)
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(512, 512, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
        (1): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(512, 512, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
        (2): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(512, 512, kernel_size=(1, 1), stride=(1, 1))
            (act): SiLU(inplace=True)
          )
          (cv2): Conv(
            (conv): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            (act): SiLU(inplace=True)
          )
        )
      )
    )
```



#### 三、Head结构

​		经过前面的BackBone结构和Neck结构，得到head1（80* 80* 256）、head2（40* 40* 512）、head3（20* 20* 1024），3个head分别通过3个卷积变为80* 80* 21，40* 40* 21、	20* 20* 21。为什么是21？因为我的分类类别数nc=2，这里的输出通道数应为3*（nc+5）

```python
    (24): Detect(
      (m): ModuleList(
        (0): Conv2d(256, 21, kernel_size=(1, 1), stride=(1, 1))
        (1): Conv2d(512, 21, kernel_size=(1, 1), stride=(1, 1))
        (2): Conv2d(1024, 21, kernel_size=(1, 1), stride=(1, 1))
      )
    )
  )
)>
class Detect(nn.Module):
    stride = None  # strides computed during build，特征图的缩放步长
    export = False  # onnx export，ONNX动态量化

    def __init__(self, nc=80, anchors=(), ch=()):  # detection layer
        super(Detect, self).__init__()
        self.nc = nc  # number of classes
        self.no = nc + 5  # number of outputs per anchor，每个类别的预测置信度+（预测类别+预测坐标）
        self.nl = len(anchors)  # number of detection layers # nl: 表示预测层数，yolov5是3层预测
        # na: 表示anchors的数量，除以2是因为[10,13, 16,30, 33,23]这个长度是6，对应3个anchor
        self.na = len(anchors[0]) // 2  # number of anchors
        # grid: 表示初始化grid列表大小，下面会计算grid，grid就是每个格子的x，y坐标（整数，比如0-19），
        # 左上角为(1,1),右下角为(input.w/stride,input.h/stride)
        self.grid = [torch.zeros(1)] * self.nl  # init grid
        # print("self.grid: ", self.grid)
        a = torch.tensor(anchors).float().view(self.nl, -1, 2)  # shape(nl,na,2)

        # 使用register_buffer方法注册anchors和anchor_grid为模块的缓冲区（buffer），
        # 这样在模型进行训练时，这些参数将被包含在模型的状态中，并且在推理过程中不会被修改。
        self.register_buffer('anchors', a)  # shape(nl,na,2)
        self.register_buffer('anchor_grid', a.clone().view(self.nl, 1, -1, 1, 1, 2))  # shape(nl,1,na,1,1,2)
        # ch=(128,256,512),最后的3个1*1卷积
        # 每一张进行三次预测，每一个预测结果包含nc+5个值
        # (n, 255, 80, 80),(n, 255, 40, 40),(n, 255, 20, 20) --> ch=(255, 255, 255)
        # 255 -> (nc+5)*3 ===> 为了提取出预测框的位置信息以及预测框尺寸信息
        self.m = nn.ModuleList(nn.Conv2d(x, self.no * self.na, 1) for x in ch)  # output conv

    def forward(self, x):
        # x = x.copy()  # for profiling
        z = []  # inference output
        self.training |= self.export
        print("self.nl", self.nl)
        # 首先进行for循环，每次i的循环，产生一个z。
        # 维度重排列：(n, 255, , ) -> (n, 3, nc+5, ny, nx) -> (n, 3, ny, nx, nc+5)，
        # 三层分别预测了80*80、40*40、20*20次。
        for i in range(self.nl):
            x[i] = self.m[i](x[i])  # conv，3个output 1*1 conv
            bs, _, ny, nx = x[i].shape  # x(bs,255,20,20) to x(bs,3,20,20,85)
            # print("ny,nx :", ny, nx)
            # print("x[i]: ", x[i].shape)   
            # 维度重排列: bs, 先验框组数, 检测框行数, 检测框列数, 属性数5 + 分类数
            x[i] = x[i].view(bs, self.na, self.no, ny, nx).permute(0, 1, 3, 4, 2).contiguous()      # .contiguous()确保张量在储存中是连续的
            # print("x[i]: ", x[i].shape)
            if not self.training:  # inference
                if self.grid[i].shape[2:4] != x[i].shape[2:4]:
                    self.grid[i] = self._make_grid(nx, ny).to(x[i].device)

# -------------------按损失函数的回归方式来转换坐标---------------------
                y = x[i].sigmoid()
                # 对坐标进行解码，计算预测框的中心坐标。
                y[..., 0:2] = (y[..., 0:2] * 2. - 0.5 + self.grid[i]) * self.stride[i]  # xy
                # 计算预测框的宽度和高度。
                y[..., 2:4] = (y[..., 2:4] * 2) ** 2 * self.anchor_grid[i]  # wh
                z.append(y.view(bs, -1, self.no))

        return x if self.training else (torch.cat(z, 1), x)

    @staticmethod
    def _make_grid(nx=20, ny=20):
        yv, xv = torch.meshgrid([torch.arange(ny), torch.arange(nx)])
        return torch.stack((xv, yv), 2).view((1, 1, ny, nx, 2)).float()

```

​		分类和 bbox 检测等都是在同一个卷积的不同通道中完成，预测结果在通道维得到。









































