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