# Orbbec SDK库总结

femto bolt官方提供了一套SDK，用于操作相机，实现二次开发。下面对使用相机SDK过程中，用到的方法进行总结。

### 获取连接到电脑的相机设备

首先要创建一个Orbbec SDK的全局上下文context，通过它才能与Orbbec设备通信，这是与所有Orbbec设备通信的入口。

```cpp
ob::Context context;
// 查询所有连接的设备
auto deviceList = context.queryDeviceList();
int deviceCount = deviceList->deviceCount();
```

通过context.queryDeviceList()就可以访问到当前连接的设备，deviceList就是当前连接在电脑上的设备列表；通过设备列表获取到当前连接的设备数量，通常通过这个信息直接判断是否有相机没有连接上；

### 配置相机参数

手动设置相机参数，包括自动曝光、

```cpp
// 相机参数配置结构体  
struct DeviceConfig {
    std::string serialNumber;
    // 彩色相机参数
    int colorExposure = 180;    // 彩色曝光  0-300
    int colorGain = 50;         // 彩色增益  0-80
    int colorBrightness = 16;   // 彩色亮度  0-20 
    int colorruidu = 20;   // 设置锐度 (int 类型)    1-40
    int colorbaohe = 200;    // 设置饱和度    1-255
    int colorcontrast = 50;    // 设置对比度    1-99


    // 深度相机参数
    //int depthExposure = 50;    // 深度曝光  0-10000
    //int depthGain = 50;         // 深度增益  0-80
    //bool OB_PROP_DEPTH_FLIP_BOOL = 1;    // 深度翻转开关 开启后，深度图像的上下翻转
    //bool OB_PROP_DEPTH_POSTFILTER_BOOL = 1;    // 深度后处理滤波开关 开启这些滤波功能可以有效减少深度图像中的噪声和孔洞，提高深度数据的连续性和准确性。
    //// 注意事项：滤波强度需要根据实际需求调整，过度滤波可能会导致细节丢失。
    //bool OB_PROP_DEPTH_HOLEFILTER_BOOL = 1;    // 深度孔洞滤波开关 
    //int OB_PROP_DEPTH_PRECISION_LEVEL_INT = 5;  // 深度精度等级 1-5，数字越大，精度越高，但是同时也会增加处理时间。
    //bool OB_PROP_DEPTH_SOFT_FILTER_BOOL = 1;   // 深度软滤波开关 
    //bool OB_PROP_FAN_WORK_MODE_INT = 0;              // 风扇工作模式 0-2
};
```

