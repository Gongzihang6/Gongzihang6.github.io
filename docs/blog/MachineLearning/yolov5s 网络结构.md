##### yolov5s 网络结构

Parameter name: epoch    Parameter value:-1
Parameter name: best_fitness     Parameter value:[    0.65574]
Parameter name: training_results         Parameter value:None
Parameter name: model    Parameter value:Model(
  (model): Sequential(
    (0): Focus(
      (conv): Conv(
        (conv): Conv2d(12, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        (bn): BatchNorm2d(32, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
    )
    (1): Conv(
      (conv): Conv2d(32, 64, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
      (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): SiLU()
    )
    (2): C3(
      (cv1): Conv(
        (conv): Conv2d(64, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(32, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv2): Conv(
        (conv): Conv2d(64, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(32, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv3): Conv(
        (conv): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(32, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(32, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(32, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(32, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
      )
    )
    (3): Conv(
      (conv): Conv2d(64, 128, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
      (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): SiLU()
    )
    (4): C3(
      (cv1): Conv(
        (conv): Conv2d(128, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv2): Conv(
        (conv): Conv2d(128, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv3): Conv(
        (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
        (1): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
        (2): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
      )
    )
    (5): Conv(
      (conv): Conv2d(128, 256, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
      (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): SiLU()
    )
    (6): C3(
      (cv1): Conv(
        (conv): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv2): Conv(
        (conv): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv3): Conv(
        (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
        (1): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
        (2): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
      )
    )
    (7): Conv(
      (conv): Conv2d(256, 512, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
      (bn): BatchNorm2d(512, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): SiLU()
    )
    (8): SPP(
      (cv1): Conv(
        (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv2): Conv(
        (conv): Conv2d(1024, 512, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(512, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (m): ModuleList(
        (0): MaxPool2d(kernel_size=5, stride=1, padding=2, dilation=1, ceil_mode=False)
        (1): MaxPool2d(kernel_size=9, stride=1, padding=4, dilation=1, ceil_mode=False)
        (2): MaxPool2d(kernel_size=13, stride=1, padding=6, dilation=1, ceil_mode=False)
      )
    )
    (9): C3(
      (cv1): Conv(
        (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv2): Conv(
        (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv3): Conv(
        (conv): Conv2d(512, 512, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(512, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
      )
    )
    (10): Conv(
      (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): SiLU()
    )
    (11): Upsample(scale_factor=2.0, mode='nearest')
    (12): Concat()
    (13): C3(
      (cv1): Conv(
        (conv): Conv2d(512, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv2): Conv(
        (conv): Conv2d(512, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv3): Conv(
        (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
      )
    )
    (14): Conv(
      (conv): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): SiLU()
    )
    (15): Upsample(scale_factor=2.0, mode='nearest')
    (16): Concat()
    (17): C3(
      (cv1): Conv(
        (conv): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv2): Conv(
        (conv): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv3): Conv(
        (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
      )
    )
    (18): Conv(
      (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
      (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): SiLU()
    )
    (19): Concat()
    (20): C3(
      (cv1): Conv(
        (conv): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv2): Conv(
        (conv): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv3): Conv(
        (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
      )
    )
    (21): Conv(
      (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
      (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): SiLU()
    )
    (22): Concat()
    (23): C3(
      (cv1): Conv(
        (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv2): Conv(
        (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (cv3): Conv(
        (conv): Conv2d(512, 512, kernel_size=(1, 1), stride=(1, 1), bias=False)
        (bn): BatchNorm2d(512, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): SiLU()
      )
      (m): Sequential(
        (0): Bottleneck(
          (cv1): Conv(
            (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
          (cv2): Conv(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
            (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
            (act): SiLU()
          )
        )
      )
    )
    (24): Detect(
      (m): ModuleList(
        (0): Conv2d(128, 21, kernel_size=(1, 1), stride=(1, 1))
        (1): Conv2d(256, 21, kernel_size=(1, 1), stride=(1, 1))
        (2): Conv2d(512, 21, kernel_size=(1, 1), stride=(1, 1))
      )
    )
  )
)
Parameter name: ema      Parameter value:None
Parameter name: updates          Parameter value:None
Parameter name: optimizer        Parameter value:None
Parameter name: wandb_id         Parameter value:None



##### 各层参数的形状

model.0.conv.conv.weight         torch.Size([32, 12, 3, 3])
model.0.conv.conv.bias   torch.Size([32])
model.1.conv.weight      torch.Size([64, 32, 3, 3])
model.1.conv.bias        torch.Size([64])
model.2.cv1.conv.weight          torch.Size([32, 64, 1, 1])
model.2.cv1.conv.bias    torch.Size([32])
model.2.cv2.conv.weight          torch.Size([32, 64, 1, 1])
model.2.cv2.conv.bias    torch.Size([32])
model.2.cv3.conv.weight          torch.Size([64, 64, 1, 1])
model.2.cv3.conv.bias    torch.Size([64])
model.2.m.0.cv1.conv.weight      torch.Size([32, 32, 1, 1])
model.2.m.0.cv1.conv.bias        torch.Size([32])
model.2.m.0.cv2.conv.weight      torch.Size([32, 32, 3, 3])
model.2.m.0.cv2.conv.bias        torch.Size([32])
model.3.conv.weight      torch.Size([128, 64, 3, 3])
model.3.conv.bias        torch.Size([128])
model.4.cv1.conv.weight          torch.Size([64, 128, 1, 1])
model.4.cv1.conv.bias    torch.Size([64])
model.4.cv2.conv.weight          torch.Size([64, 128, 1, 1])
model.4.cv2.conv.bias    torch.Size([64])
model.4.cv3.conv.weight          torch.Size([128, 128, 1, 1])
model.4.cv3.conv.bias    torch.Size([128])
model.4.m.0.cv1.conv.weight      torch.Size([64, 64, 1, 1])
model.4.m.0.cv1.conv.bias        torch.Size([64])
model.4.m.0.cv2.conv.weight      torch.Size([64, 64, 3, 3])
model.4.m.0.cv2.conv.bias        torch.Size([64])
model.4.m.1.cv1.conv.weight      torch.Size([64, 64, 1, 1])
model.4.m.1.cv1.conv.bias        torch.Size([64])
model.4.m.1.cv2.conv.weight      torch.Size([64, 64, 3, 3])
model.4.m.1.cv2.conv.bias        torch.Size([64])
model.4.m.2.cv1.conv.weight      torch.Size([64, 64, 1, 1])
model.4.m.2.cv1.conv.bias        torch.Size([64])
model.4.m.2.cv2.conv.weight      torch.Size([64, 64, 3, 3])
model.4.m.2.cv2.conv.bias        torch.Size([64])
model.5.conv.weight      torch.Size([256, 128, 3, 3])
model.5.conv.bias        torch.Size([256])
model.6.cv1.conv.weight          torch.Size([128, 256, 1, 1])
model.6.cv1.conv.bias    torch.Size([128])
model.6.cv2.conv.weight          torch.Size([128, 256, 1, 1])
model.6.cv2.conv.bias    torch.Size([128])
model.6.cv3.conv.weight          torch.Size([256, 256, 1, 1])
model.6.cv3.conv.bias    torch.Size([256])
model.6.m.0.cv1.conv.weight      torch.Size([128, 128, 1, 1])
model.6.m.0.cv1.conv.bias        torch.Size([128])
model.6.m.0.cv2.conv.weight      torch.Size([128, 128, 3, 3])
model.6.m.0.cv2.conv.bias        torch.Size([128])
model.6.m.1.cv1.conv.weight      torch.Size([128, 128, 1, 1])
model.6.m.1.cv1.conv.bias        torch.Size([128])
model.6.m.1.cv2.conv.weight      torch.Size([128, 128, 3, 3])
model.6.m.1.cv2.conv.bias        torch.Size([128])
model.6.m.2.cv1.conv.weight      torch.Size([128, 128, 1, 1])
model.6.m.2.cv1.conv.bias        torch.Size([128])
model.6.m.2.cv2.conv.weight      torch.Size([128, 128, 3, 3])
model.6.m.2.cv2.conv.bias        torch.Size([128])
model.7.conv.weight      torch.Size([512, 256, 3, 3])
model.7.conv.bias        torch.Size([512])
model.8.cv1.conv.weight          torch.Size([256, 512, 1, 1])
model.8.cv1.conv.bias    torch.Size([256])
model.8.cv2.conv.weight          torch.Size([512, 1024, 1, 1])
model.8.cv2.conv.bias    torch.Size([512])
model.9.cv1.conv.weight          torch.Size([256, 512, 1, 1])
model.9.cv1.conv.bias    torch.Size([256])
model.9.cv2.conv.weight          torch.Size([256, 512, 1, 1])
model.9.cv2.conv.bias    torch.Size([256])
model.9.cv3.conv.weight          torch.Size([512, 512, 1, 1])
model.9.cv3.conv.bias    torch.Size([512])
model.9.m.0.cv1.conv.weight      torch.Size([256, 256, 1, 1])
model.9.m.0.cv1.conv.bias        torch.Size([256])
model.9.m.0.cv2.conv.weight      torch.Size([256, 256, 3, 3])
model.9.m.0.cv2.conv.bias        torch.Size([256])
model.10.conv.weight     torch.Size([256, 512, 1, 1])
model.10.conv.bias       torch.Size([256])
model.13.cv1.conv.weight         torch.Size([128, 512, 1, 1])
model.13.cv1.conv.bias   torch.Size([128])
model.13.cv2.conv.weight         torch.Size([128, 512, 1, 1])
model.13.cv2.conv.bias   torch.Size([128])
model.13.cv3.conv.weight         torch.Size([256, 256, 1, 1])
model.13.cv3.conv.bias   torch.Size([256])
model.13.m.0.cv1.conv.weight     torch.Size([128, 128, 1, 1])
model.13.m.0.cv1.conv.bias       torch.Size([128])
model.13.m.0.cv2.conv.weight     torch.Size([128, 128, 3, 3])
model.13.m.0.cv2.conv.bias       torch.Size([128])
model.14.conv.weight     torch.Size([128, 256, 1, 1])
model.14.conv.bias       torch.Size([128])
model.17.cv1.conv.weight         torch.Size([64, 256, 1, 1])
model.17.cv1.conv.bias   torch.Size([64])
model.17.cv2.conv.weight         torch.Size([64, 256, 1, 1])
model.17.cv2.conv.bias   torch.Size([64])
model.17.cv3.conv.weight         torch.Size([128, 128, 1, 1])
model.17.cv3.conv.bias   torch.Size([128])
model.17.m.0.cv1.conv.weight     torch.Size([64, 64, 1, 1])
model.17.m.0.cv1.conv.bias       torch.Size([64])
model.17.m.0.cv2.conv.weight     torch.Size([64, 64, 3, 3])
model.17.m.0.cv2.conv.bias       torch.Size([64])
model.18.conv.weight     torch.Size([128, 128, 3, 3])
model.18.conv.bias       torch.Size([128])
model.20.cv1.conv.weight         torch.Size([128, 256, 1, 1])
model.20.cv1.conv.bias   torch.Size([128])
model.20.cv2.conv.weight         torch.Size([128, 256, 1, 1])
model.20.cv2.conv.bias   torch.Size([128])
model.20.cv3.conv.weight         torch.Size([256, 256, 1, 1])
model.20.cv3.conv.bias   torch.Size([256])
model.20.m.0.cv1.conv.weight     torch.Size([128, 128, 1, 1])
model.20.m.0.cv1.conv.bias       torch.Size([128])
model.20.m.0.cv2.conv.weight     torch.Size([128, 128, 3, 3])
model.20.m.0.cv2.conv.bias       torch.Size([128])
model.21.conv.weight     torch.Size([256, 256, 3, 3])
model.21.conv.bias       torch.Size([256])
model.23.cv1.conv.weight         torch.Size([256, 512, 1, 1])
model.23.cv1.conv.bias   torch.Size([256])
model.23.cv2.conv.weight         torch.Size([256, 512, 1, 1])
model.23.cv2.conv.bias   torch.Size([256])
model.23.cv3.conv.weight         torch.Size([512, 512, 1, 1])
model.23.cv3.conv.bias   torch.Size([512])
model.23.m.0.cv1.conv.weight     torch.Size([256, 256, 1, 1])
model.23.m.0.cv1.conv.bias       torch.Size([256])
model.23.m.0.cv2.conv.weight     torch.Size([256, 256, 3, 3])
model.23.m.0.cv2.conv.bias       torch.Size([256])
model.24.m.0.weight      torch.Size([21, 128, 1, 1])
model.24.m.0.bias        torch.Size([21])
model.24.m.1.weight      torch.Size([21, 256, 1, 1])
model.24.m.1.bias        torch.Size([21])
model.24.m.2.weight      torch.Size([21, 512, 1, 1])
model.24.m.2.bias        torch.Size([21])



##### 输入为640* 640* 3时，各层输出形状

###### Layer (type:depth-idx)                        Output Shape              Param #

Model                                         [1, 25200, 7]             --
├─Sequential: 1-1                             --                        --
│    └─Focus: 2-1                             [1, 32, 320, 320]         --
│    │    └─Conv: 3-1                         [1, 32, 320, 320]         (3,488)
│    └─Conv: 2-2                              [1, 64, 160, 160]         --
│    │    └─Conv2d: 3-2                       [1, 64, 160, 160]         (18,496)
│    │    └─SiLU: 3-3                         [1, 64, 160, 160]         --
│    └─C3: 2-3                                [1, 64, 160, 160]         --
│    │    └─Conv: 3-4                         [1, 32, 160, 160]         (2,080)
│    │    └─Sequential: 3-5                   [1, 32, 160, 160]         (10,304)
│    │    └─Conv: 3-6                         [1, 32, 160, 160]         (2,080)
│    │    └─Conv: 3-7                         [1, 64, 160, 160]         (4,160)
│    └─Conv: 2-4                              [1, 128, 80, 80]          --
│    │    └─Conv2d: 3-8                       [1, 128, 80, 80]          (73,856)
│    │    └─SiLU: 3-9                         [1, 128, 80, 80]          --
│    └─C3: 2-5                                [1, 128, 80, 80]          --
│    │    └─Conv: 3-10                        [1, 64, 80, 80]           (8,256)
│    │    └─Sequential: 3-11                  [1, 64, 80, 80]           (123,264)
│    │    └─Conv: 3-12                        [1, 64, 80, 80]           (8,256)
│    │    └─Conv: 3-13                        [1, 128, 80, 80]          (16,512)
│    └─Conv: 2-6                              [1, 256, 40, 40]          --
│    │    └─Conv2d: 3-14                      [1, 256, 40, 40]          (295,168)
│    │    └─SiLU: 3-15                        [1, 256, 40, 40]          --
│    └─C3: 2-7                                [1, 256, 40, 40]          --
│    │    └─Conv: 3-16                        [1, 128, 40, 40]          (32,896)
│    │    └─Sequential: 3-17                  [1, 128, 40, 40]          (492,288)
│    │    └─Conv: 3-18                        [1, 128, 40, 40]          (32,896)
│    │    └─Conv: 3-19                        [1, 256, 40, 40]          (65,792)
│    └─Conv: 2-8                              [1, 512, 20, 20]          --
│    │    └─Conv2d: 3-20                      [1, 512, 20, 20]          (1,180,160)
│    │    └─SiLU: 3-21                        [1, 512, 20, 20]          --
│    └─SPP: 2-9                               [1, 512, 20, 20]          --
│    │    └─Conv: 3-22                        [1, 256, 20, 20]          (131,328)
│    │    └─ModuleList: 3-23                  --                        --
│    │    └─Conv: 3-24                        [1, 512, 20, 20]          (524,800)
│    └─C3: 2-10                               [1, 512, 20, 20]          --
│    │    └─Conv: 3-25                        [1, 256, 20, 20]          (131,328)
│    │    └─Sequential: 3-26                  [1, 256, 20, 20]          (655,872)
│    │    └─Conv: 3-27                        [1, 256, 20, 20]          (131,328)
│    │    └─Conv: 3-28                        [1, 512, 20, 20]          (262,656)
│    └─Conv: 2-11                             [1, 256, 20, 20]          --
│    │    └─Conv2d: 3-29                      [1, 256, 20, 20]          (131,328)
│    │    └─SiLU: 3-30                        [1, 256, 20, 20]          --
│    └─Upsample: 2-12                         [1, 256, 40, 40]          --
│    └─Concat: 2-13                           [1, 512, 40, 40]          --
│    └─C3: 2-14                               [1, 256, 40, 40]          --
│    │    └─Conv: 3-31                        [1, 128, 40, 40]          (65,664)
│    │    └─Sequential: 3-32                  [1, 128, 40, 40]          (164,096)
│    │    └─Conv: 3-33                        [1, 128, 40, 40]          (65,664)
│    │    └─Conv: 3-34                        [1, 256, 40, 40]          (65,792)
│    └─Conv: 2-15                             [1, 128, 40, 40]          --
│    │    └─Conv2d: 3-35                      [1, 128, 40, 40]          (32,896)
│    │    └─SiLU: 3-36                        [1, 128, 40, 40]          --
│    └─Upsample: 2-16                         [1, 128, 80, 80]          --
│    └─Concat: 2-17                           [1, 256, 80, 80]          --
│    └─C3: 2-18                               [1, 128, 80, 80]          --
│    │    └─Conv: 3-37                        [1, 64, 80, 80]           (16,448)
│    │    └─Sequential: 3-38                  [1, 64, 80, 80]           (41,088)
│    │    └─Conv: 3-39                        [1, 64, 80, 80]           (16,448)
│    │    └─Conv: 3-40                        [1, 128, 80, 80]          (16,512)
│    └─Conv: 2-19                             [1, 128, 40, 40]          --
│    │    └─Conv2d: 3-41                      [1, 128, 40, 40]          (147,584)
│    │    └─SiLU: 3-42                        [1, 128, 40, 40]          --
│    └─Concat: 2-20                           [1, 256, 40, 40]          --
│    └─C3: 2-21                               [1, 256, 40, 40]          --
│    │    └─Conv: 3-43                        [1, 128, 40, 40]          (32,896)
│    │    └─Sequential: 3-44                  [1, 128, 40, 40]          (164,096)
│    │    └─Conv: 3-45                        [1, 128, 40, 40]          (32,896)
│    │    └─Conv: 3-46                        [1, 256, 40, 40]          (65,792)
│    └─Conv: 2-22                             [1, 256, 20, 20]          --
│    │    └─Conv2d: 3-47                      [1, 256, 20, 20]          (590,080)
│    │    └─SiLU: 3-48                        [1, 256, 20, 20]          --
│    └─Concat: 2-23                           [1, 512, 20, 20]          --
│    └─C3: 2-24                               [1, 512, 20, 20]          --
│    │    └─Conv: 3-49                        [1, 256, 20, 20]          (131,328)
│    │    └─Sequential: 3-50                  [1, 256, 20, 20]          (655,872)
│    │    └─Conv: 3-51                        [1, 256, 20, 20]          (131,328)
│    │    └─Conv: 3-52                        [1, 512, 20, 20]          (262,656)
│    └─Detect: 2-25                           [1, 25200, 7]             --

###### │    │    └─ModuleList: 3-53                  --                        (18,879)