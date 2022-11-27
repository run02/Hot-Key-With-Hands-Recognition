# 自动训练模型

## 工程结构简介

![image-20221127233511417](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221127233511417.png)

## 如何使用

1. 只需围绕想要的手势拍摄视频,然后在`GestureVideos`目录下建立文件夹(一种手势一个),然后把对应的视频文件放入到对应的文件夹中即可. 比如说这样:

![image-20221127234028068](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221127234028068.png)

2. 运行主函数,结束后您将会得到训练出的模型.训练结束后会运行测试代码,会在窗口中显示预测的结果和概率. 视频时间长,动作角度多,可以提高识别的精度. 

   生成的模型文件将会在`ModelFiles`目录下

   ![image-20221127234422638](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221127234422638.png)

   您可以通过这样的方式获得对应的手势和模型文件

   ```python
   ges= np.load(resource_path('DataForTraining/all_gestures.npy'),allow_pickle=True).tolist()
   
   model = load_model(resource_path('TrainingOutput/ModelFiles'))  # 加载训练好的tensorflow模型
   ```



这里只是搭了一个自动训练的框架, 您可以根据自己的喜好替换为自己想要的内容.

## 实现的思路

1. 读取视频的文件位置,得到需要训练的手势是哪些与文件的位置
2. 调用`mediapipe`通过播放提前录制好的视频,按照顺序生成训练集
3. 定义模型, 然后将视频生成的训练集带入模型中训练
4. 保存模型,并测试运行效果

## TODO

目前这里属于一个能用但是需要改进的草稿版本,,受限于时间和作者的水平, 它有很多可以优化和升级的地方.

- 使用`numpy`数组代替`list`可以获得更好的性能
- 生成训练集的部分可以增加断点续训的功能,通过记录当前训练的位置实现
- 训练的部分可以增加断点续训和`tensorboard`统计的功能
- 可以使用`PyQT5`制作界面, 更方便用户操作.
- 可以把手势识别快捷键的应用和训练的应用集成到一起
- 可以使用更好的模型(hard)
- 基于双手识别结果和控制鼠标的操作支持