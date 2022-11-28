# **[Hot-Key-With-Hands-Recognition](https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition)**

**Switch Language**: [切换到中文简体](https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition/tree/V0.1.0-zh)

With this software, you can operate and browse TikTtok(in web browser or software on windows) while eating a burger without worrying about dirtying the keyboard or mouse with food crumbs on your hands.

Controlling objects in the air has always been a fantasy thing, using this software, controlling objects in the air will not be far away.

## Introduction

This is an app that binds shortcut keys based on gesture recognition.

It can recognize your gestures, and then trigger the corresponding shortcut keys according to the recognized gestures to realize customized functions.

For example [Browse Tik Tok](https://www.youtube.com/watch?v=vOSos8CcdtQ):

[You can click this link to view the demo effect of the program.](https://www.youtube.com/watch?v=vOSos8CcdtQ)

According to the eleven shortcut gestures provided, you can easily implement customized functions.

You can download the packaged .`exe` file in [releases](https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition/releases), which can be run directly on the windows system ( The speed of operation depends on the performance of your CPU).

There are currently two versions in Chinese and English.



About the training of the model, you can enter the [training branch](https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition/tree/training) to view. Maybe In the future this branch will fork into main branch.



### The gestures currently supported for recognition are as follows:

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



#### software UI

![image-20221123021011573](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221123021011573.png)

You can modify the shortcut key corresponding to the gesture in the edit box, like this:

Among them, `up` corresponds to the `↑` key on the keyboard, and other keys only need to enter the corresponding names.

![image-20221123021120895](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221123021120895.png)

## My Solution

Using `mediapipe.hands` to get the coordinates of 21 hand joints,

Using `tensorflow.kears` to train a gesture recognition model based on 21 joint coordinates, and predict.

Using`keyboard` to implement shortcut key events that trigger corresponding gestures.

Using`QyQt5` to implement user interaction page.

Using `QT-Material` to achieve cool UI themes.

Using `auto-py-to-exe` to operate `pyinstaller` to achieve `.exe application` packaging.

From the code statistics of `cloc` statistics, the total code of this project is less than 300 lines, which can be regarded as a lightweight application.

![image-20221123011608429](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221123011608429.png)

## Project structure 

![image-20221123021812038](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221123021812038.png)

## Unresolved Issues

- Limited by the author's level, there are many problems in this project. At present, the following points are the most fatal:

- The packaged `.exe file` is too large, it feels like it doesn’t have many functions, but it takes up nearly 400MB of memory. It feels really bloated.

- Gesture recognition is unstable

  When training the model, I use my own hand, and most of it is centered on the camera, so the trained model does not seem to recognize other hands, and there are many errors in the recognition results at positions off the center of the camera.

  poor model quality

  Limited by my level, the core of the trained model has no more than one convolution kernel, which is the best model I can think of.

- There are still many problems that the author is not aware of and need to be corrected.

## Thanks to

Many thanks to the following institutions or authors, without whom this project would be difficult or impossible to do.

[Home | mediapipe (google.github.io)](https://google.github.io/mediapipe/)

[关于TensorFlow | TensorFlow中文官网 (google.cn)](https://tensorflow.google.cn/)

[人工智能实践：Tensorflow笔记_北京大学_中国大学MOOC(慕课) (icourse163.org)](https://www.icourse163.org/course/PKU-1002536002?from=searchPage&outVendor=zw_mooc_pcssjg_)

[PyCharm: the Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/)

[GitHub - boppreh/keyboard: Hook and simulate global keyboard events on Windows and Linux.](https://github.com/boppreh/keyboard)

[PyQt5 · PyPI](https://pypi.org/project/PyQt5/)

[Qt-Material — Qt Material documentation](https://qt-material.readthedocs.io/en/latest/index.html)

[PyInstaller Manual — PyInstaller 5.6.2 documentation](https://pyinstaller.org/en/stable/)

[auto-py-to-exe · PyPI](https://pypi.org/project/auto-py-to-exe/)

[Google Translate](https://translate.google.com)



I also thank my mentor. I used to be a person who could hardly write code. He encouraged me when I was confused and confused. It was this support that made me go on the road of programming and solve problems step by step. Coding ability. Although my level of writing code is average now, for me, this is already a huge breakthrough. From a person who can't even learn C language, to now I can freely realize what I want. It's simply unimaginable.

There are also many thanks to blog  authors that can search for solutions when encountering bugs.



## Special Statement

The author is still a rookie when he finished writing this project, if there is any problem, please bear with us~

Everyone is welcome to point out the problems in the project, there is a 50% probability that they will be resolved in time~
