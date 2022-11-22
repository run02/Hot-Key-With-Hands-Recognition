# 手势识别绑定快捷键

使用这款软件，您可以在吃汉堡的同时刷抖音（在网络浏览器或Windows软件中），而不必担心手上的食物碎屑会弄脏键盘或鼠标。或者是根据您设置的快捷键,完成指定的事情.

隔空控物一直是一件玄幻的事情,使用这款软件,隔空控物将不在遥远.

## 简介

这是一款基于手势识别绑定快捷键的应用.

他可以识别出你的手势,然后根据识别出的接过,触发对应的快捷键,实现自定义的功能.

比如说[隔空刷抖音](https://www.douyin.com/user/MS4wLjABAAAAy5YUmt3PiQaZEP4GWYRROU2e-SrIzUv0yAqIiZxfbHw?modal_id=7168877845723352357):

[您可以点击这个链接查看程序演示效果.](https://www.douyin.com/user/MS4wLjABAAAAy5YUmt3PiQaZEP4GWYRROU2e-SrIzUv0yAqIiZxfbHw?modal_id=7168877845723352357)

根据提供的十一个快捷手势,您可以轻松实现自定义的功能.

您可以在`release`中下载已经打包好的.`exe`文件,它可以在windows系统上直接运行(运行的速度取决于您CPU的性能).

目前提供中文和英文两个版本.

### 目前支持识别的手势有如下这些

<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps1.jpg" alt="img" style="zoom:50%;" /> 



 

<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps2.jpg" alt="img" style="zoom:50%;" /> 



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps3.jpg" alt="img" style="zoom:50%;" /> 



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps4.jpg" alt="img" style="zoom:50%;" /> 



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps5.jpg" alt="img" style="zoom:50%;" /> 



 

<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps6.jpg" alt="img" style="zoom:50%;" /> 



 

<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps7.jpg" alt="img" style="zoom:50%;" /> 



 

 

<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps8.jpg" alt="img" style="zoom:50%;" /> 



 

 

<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps9.jpg" alt="img" style="zoom:50%;" /> 



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps10.jpg" alt="img" style="zoom:50%;" /> 



 

<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//wps11.jpg" alt="img" style="zoom:50%;" /> 



#### 软件界面

![image-20221123005622791](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221123005622791.png)

可以在编辑框中修改手势对应的快捷键,像是这样:

其中`up`对应键盘上的`↑`键,其它按键只需要输入对应的名称即可.

![image-20221123005946819](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221123005946819.png)

## 实现的方案

调用`mediapipe.hands`获得21个手部关节的坐标,

使用`tensorflow.kears`根据21个关节坐标训练手势识别模型,与预测.

使用`keyboard`实现触发对应手势的快捷键事件.

使用`QyQt5`实现用户交互页面.

使用`QT-Material`实现炫酷的UI主题.

使用`auto-py-to-exe`操作`pyinstaller`实现`.exe应用`打包.

从`cloc`统计的代码统计来看,本项目共计代码不到300行,算是一个轻量级的应用.

![image-20221123011608429](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221123011608429.png)

## 项目的工程结构

![image-20221123013141329](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221123013141329.png)

## 待解决的问题

受限于作者的水平,该项目存在很多问题,目前有以下几点感觉最为致命:

- 打包后的`.exe文件`过大,感觉明明没多少功能,却占用了将近400MB内存.感觉实在是臃肿.

- 手势识别不稳定

  训练模型的时候用的是自己的手,且多半以摄像头为中心,导致训练出的模型好像不太认识别的手,并且在偏离摄像头中心的位置识别出的结果有很多误差.

- 模型质量较差

  受限于我的水平,训练出的模型核心只有不超过一个卷积核,这已经我能想到的最好的模型了.

- 还有很多作者并没有意识到的问题,有待更正.

## 鸣谢

非常感谢以下的机构或者作者,如果没有他们这个项目将很难或者不可能做的出来.

[Home | mediapipe (google.github.io)](https://google.github.io/mediapipe/)

[关于TensorFlow | TensorFlow中文官网 (google.cn)](https://tensorflow.google.cn/)

[人工智能实践：Tensorflow笔记_北京大学_中国大学MOOC(慕课) (icourse163.org)](https://www.icourse163.org/course/PKU-1002536002?from=searchPage&outVendor=zw_mooc_pcssjg_)

[PyCharm: the Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/)

[GitHub - boppreh/keyboard: Hook and simulate global keyboard events on Windows and Linux.](https://github.com/boppreh/keyboard)

[PyQt5 · PyPI](https://pypi.org/project/PyQt5/)

[Qt-Material — Qt Material documentation](https://qt-material.readthedocs.io/en/latest/index.html)

同样也感谢我的导师,我曾经是一个几乎写不出代码的人,在我困惑和迷茫的时候给予我鼓励,正是这份支持使得我在编程的道路上走下去,一步步解决问题提高编码的能力.虽然我现在写代码的水平一般般,但对于我来说,这已经算是一种巨大的突破了,从一个连c语言都学不懂的人,到现在能自由的实现自己想要的代码,这简直是难以想象.

还有很多的博客的作者,在碰到bug的时候一下就能搜索出解决方案.



## 特别声明

作者目前写完这个项目的时候还是个菜鸟,如果哪里有问题的话还请大家多多担待啊~

欢迎大家指出项目中的问题,有50%的概率会得到及时的解决~