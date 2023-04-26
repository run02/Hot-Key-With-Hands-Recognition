# 手势识别快捷键

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![Version](https://img.shields.io/badge/version-0.2.0-brightgreen)]()[![Multi-Language](https://img.shields.io/badge/multi--language-supported-blue)]()

:globe_with_meridians: [English](README.md) |[中文](README-zh.md)

## 简介

这是一款基于手势识别绑定快捷键的应用.可以根据摄像头识别出的手势,触发指定的快捷键. 通过这个功能可以实现类似于隔空控物的效果.

比如说隔空刷抖音:

[您可以点击这个链接查看程序演示效果(这个是老版本的,新版本的正在制作)](https://www.bilibili.com/video/BV1RM411r7X6/?spm_id_from=333.999.0.0)

您可以在[releases](https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition/releases)中下载已经打包好的.`exe`文件,或者通过源码运行.

您也可以通过训练模型的[分支](https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition/tree/training-zh)训练自己的手势识别模型,或者实现抽象接口构建自己的手势识别模型.

## 软件界面与使用方式

### 主界面:

![image-20230426133300685](readme_assets/image-20230426133300685.png)

### 选择语言:

![image-20230426140032428](readme_assets/image-20230426140032428.png)

![image-20230426135831114](readme_assets/image-20230426135831114.png)

### 设置手势对应的快捷键:

![image-20230426133335028](readme_assets/image-20230426133335028.png)

### 保存:

![image-20230426133345015](readme_assets/image-20230426133345015.png)

### 当前模型可能能识别出的手势

 ![eight.ico](assets\gestures_icons\eight.ico)  ![cool.ico](assets\gestures_icons\cool.ico)  ![fist.ico](assets\gestures_icons\fist.ico)  ![five.ico](assets\gestures_icons\five.ico)  ![four.ico](assets\gestures_icons\four.ico)  ![fuck.ico](assets\gestures_icons\fuck.ico)  ![nine.ico](assets\gestures_icons\nine.ico) ![one.ico](assets\gestures_icons\one.ico)  ![seven.ico](assets\gestures_icons\seven.ico)  ![six.ico](assets\gestures_icons\six.ico)  ![three.ico](assets\gestures_icons\three.ico)  ![two.ico](assets\gestures_icons\two.ico) 

 

## 安装和运行

- 使用打包好的可执行文件运行

  进入releases,下载`gesture2shortcuts.exe`,点击即可运行

  注: 目前只打包好了Windows版本, Linux版本或Mac版本需要使用从源码构建的方式

- 从源码构建

  ```sh
  #下载并安装环境
  git clone https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition.git
  cd Hot-Key-With-Hands-Recognition
  pip3 install -r requirements.py
  #运行APP
  python3 main.py
  ```

## 项目结构

![image-20230426164241983](readme_assets/image-20230426164241983.png)





## 关于贡献代码

非常乐意看到您对这个仓库感兴趣并且愿意为之贡献代码.  非常欢迎您来贡献代码, 包括但不限于以下部分:

### 可贡献的内容

- 贡献手势识别模型

- 贡献手势训练的脚本
- 贡献软件架构与抽象

- 贡献用户界面

- 贡献图标
- 贡献翻译
- 贡献演示视频

- 贡献其它内容

### 步骤

1. 在 GitHub 上 fork 该项目。
2. 克隆 fork 后的仓库到本地，可以使用以下命令：

```sh
git clone https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition.git
```

3. 创建一个新的分支，并在该分支上进行开发，可以使用以下命令：

```sh
git checkout -b your_feature_branch
```

4. 在本地测试并确保代码质量。确保你的代码符合项目的质量标准，包括代码风格、变量命名规范、注释规范等，具体规范见下文。

5. 提交代码到 fork 后的仓库，可以使用以下命令：

```sh
git add .
git commit -m "Your commit message"
git push origin your_feature_branch
```

6. 在 GitHub上创建一个 Pull Request。在 Pull Request 中简要描述你所做的更改，并附上相应的截图或者示例。

### 规范

- 代码风格：建议使用 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 作为代码风格指南。

- 变量及函数规范：尽量使用标准且通用的英语来命名变量, 最好是使用跟本仓库相似的命名风格.

- 提交信息规范：

  您可以参考以下格式:

  ```txt
  English Title / 中文标题
  
  The purpose of the commit and the changes made
  
  提交的目的和所做的更改
  
  Author: 作者名字
  
  Date: 提交日期
  ```

## 版本更新记录

### V0.2.0

- 架构升级, 采用分层设计

- 增加了多语言的支持, 目前支持简体中文,繁体中文,英语

  由于Qt自带的翻译需要下载太多内容比较麻烦, 这里单独实现了一个支持多语言轻量级的翻译方式

- 快捷键绑定设置优化, 由手动输入变成点击后自动捕获按下的快捷键

- 快捷键绑定界面优化, 用改用图片代替文字展示手势

- 增加了是否展示摄像头的选项

- UI界面优化

  ![image-20230426133300685](readme_assets/image-20230426133300685.png)

  ![image-20230426140032428](readme_assets/image-20230426140032428.png)

  

![image-20230426133335028](readme_assets/image-20230426133335028.png)



![image-20230426133345015](readme_assets/image-20230426133345015.png)



![image-20230426135831114](readme_assets/image-20230426135831114.png)



### V0.1.0

![img](readme_assets/68747470733a2f2f6d792d626c6f67732d696d67732d313331323534363136372e636f732e61702d6e616e6a696e672e6d7971636c6f75642e636f6d2f2f696d6167652d32303232313132333032313031313537332e706e67.png)

<img src="readme_assets/68747470733a2f2f6d792d626c6f67732d696d67732d313331323534363136372e636f732e61702d6e616e6a696e672e6d7971636c6f75642e636f6d2f2f696d6167652d32303232313132333030353632323739312e706e67.png" alt="img" style="zoom: 67%;" />

## 下一个版本的更新预告

未来有可能在某段时间通过以下方式进行更新

### 功能更新预告

- #### 智能家居与物联网

  目前识别发送出的信号仅限于触发相应的快捷键

  在这个软件发布前已经制作出了使用手势控制进行隔空开灯的草稿, 但那个草稿的软件结构几乎没有, 并且存在很多安全问题, 进一步的想法是搭建一个物联网系统, 并将其接入到该系统内.

### 界面更新预告

- #### 界面主题设置功能

  预计会在.qss文件内提供多套组件的UI方案, 可以选择相应的主题

- #### 更完备的设置功能

### 架构更新预告

- 提供更完备的分层与抽象

### 体积压缩预告

- 考虑使用C++或使用更轻量级的模型框架,以减少打包后的体积

## 鸣谢

[ChatGPT](https://chat.openai.com)

[Home | mediapipe (google.github.io)](https://google.github.io/mediapipe/)

[TensorFlow](https://tensorflow.google.cn/)

[PyCharm: the Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/)

[GitHub - boppreh/keyboard: Hook and simulate global keyboard events on Windows and Linux.](https://github.com/boppreh/keyboard)

[PyQt5 · PyPI](https://pypi.org/project/PyQt5/)

[Qt-Material — Qt Material documentation](https://qt-material.readthedocs.io/en/latest/index.html)

[PyInstaller Manual — PyInstaller 5.6.2 documentation](https://pyinstaller.org/en/stable/)

[auto-py-to-exe · PyPI](https://pypi.org/project/auto-py-to-exe/)