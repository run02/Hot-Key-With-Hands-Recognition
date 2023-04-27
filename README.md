# Gesture Recognition Shortcuts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Version](https://img.shields.io/badge/version-0.2.0-brightgreen)](?model=text-davinci-002-render-sha) [![Multi-Language](https://img.shields.io/badge/multi--language-supported-blue)](?model=text-davinci-002-render-sha)

:globe_with_meridians: **Supported Languages**: [English](README.md) | [中文](README-zh.md)

## Introduction

This gesture recognition-based software enables you to effortlessly operate and browse various applications on your Windows computer without the need for a keyboard or mouse, such as [effortlessly swiping through TikTok](README_DEMO_VIDEOS.md).Whether you're enjoying a meal, have messy hands, or are just a bit far from your computer, you can rely on gesture recognition to control the app and experience the convenience of touch-free navigation. The camera detects gestures, which then trigger corresponding shortcuts.

You can download the pre-packaged `.exe` file in [releases](https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition/releases), or run it through the source code.

You can also train your own gesture recognition model through the [training branch](https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition/tree/training) or build your own gesture recognition model by implementing the abstract interface.

## Software Interface and Usage

### Main Interface:

![image-20230426133300685](readme_assets/mainWindow.png)



### Language Selection:

![image-20230426140032428](readme_assets/langueSetting.png)

![image-20230426133335028](readme_assets/cn.png)

### Set the corresponding shortcut for the gesture:

![image-20230426133345015](readme_assets/setting_key.png)

### Save:

![image-20230426135831114](readme_assets/modified.png)

### Gestures that the current model may recognize

![image-20230427003059769](readme_assets/image-20230427003059769.png)

## Installation and Running

- Run using pre-packaged executable file

  Go to releases and download `gesture2shortcuts.exe`, and click to run.

  Note: Currently only the Windows version has been packaged, the Linux or Mac version needs to be built from the source code.

- Build from source code

  ```sh
  # download and install environment
  git clone https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition.git
  cd Hot-Key-With-Hands-Recognition
  pip3 install -r requirements.py
  # run the app
  python3 main.py
  ```

## Project Structure

![image-20230427010212580](readme_assets/image-20230427010212580.png)

### Contributable Content

- Gesture recognition models

  Commit changes to the `saved_ai_model` or `saved_ai_lite_model` directories.

- Gesture training scripts

  Commit changes to the `training` branch.

- Software architecture and abstraction

  Commit changes to the `abstract_layer.py` file.

- User interface

  Commit changes to the `assets/styles` directory.

- Icons

  Commit changes to the `assets/gestures_icons` directory or any other directory.

- Translations

  Commit changes to the `assets/translations.yml` file.

  ```yaml
  supported_languages:
    - en
    - zh-CN
    - zh-TW
  #add new supported language here such as -JP
  
  translations:
    Language:
      en: Language
      zh-CN: 语言
      zh-TW: 語言
  #then trannslate the key and add new key and value such as JP: 言語
  
    Start:
      en: Start
      zh-CN: 开始
      zh-TW: 開始
  
    Stop:
      en: Stop
      zh-CN: 停止
      zh-TW: 停止
  ```

- Demo videos

  Commit changes to the `README_DEMO_VIDEOS.md` file.

- Other content

  Commit changes to any other directory.

### Steps

1. Fork this project on GitHub.

2. Clone the forked repository locally using the following command:

   ```bash
   git clone https://github.com/LiRunJi/Hot-Key-With-Hands-Recognition.git
   ```

3. Create a new branch and start developing on it. You can use the following command:

   ```sh
   git checkout -b your_feature_branch
   ```

4. Test the changes locally and make sure the code quality is good. Ensure that your code meets the quality standards of the project, including coding style, variable naming conventions, and comment conventions, etc., as specified below.

5. Commit the changes to the forked repository using the following command:

   ```sh
   git add .
   git commit -m "Your commit message"
   git push origin your_feature_branch
   ```

6. Create a pull request on GitHub. In the pull request, briefly describe the changes you made and provide relevant screenshots or examples.

### Standards

- Coding style: We recommend following the [PEP 8](https://www.python.org/dev/peps/pep-0008/) coding style guide.

- Variable and function specifications: Use standard and common English to name variables as much as possible. It is best to use a naming style similar to that of this repository.

- Commit message specifications:

  We recommend the following format for commit messages:

  ```
  Title 
  
  The purpose of the commit and the changes made
  
  Author: your name 
  
  Date: 0000-00-00
  ```

## [Version History](CHANGELOG.md)

## Next Version Preview

It is possible that the next update will be released at some point in the future through the following means.

### Function Update Preview

- #### Smart Home and IoT

  Currently, the recognition of the signals sent is limited to triggering the corresponding shortcuts.

  Before this software was released, a draft of using gestures to control lighting remotely was made, but the software structure of that draft was almost non-existent, and there were many security issues. Further ideas include building an IoT system and integrating it into this system.

### Interface Update Preview

- #### Interface Theme Setting Function

  It is expected to provide multiple sets of UI schemes in the .qss file, and you can choose the appropriate theme.

- #### More comprehensive setting function

### Architecture Update Preview

- Provide more comprehensive layering and abstraction.

### Volume Compression Preview

- Consider using C++ or a lighter model framework to reduce the size after packaging.

  

## Thanks to

[ChatGPT](https://chat.openai.com)

[Home | mediapipe (google.github.io)](https://google.github.io/mediapipe/)

[TensorFlow](https://tensorflow.google.cn/)

[PyCharm: the Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/)

[GitHub - boppreh/keyboard: Hook and simulate global keyboard events on Windows and Linux.](https://github.com/boppreh/keyboard)

[PyQt5 · PyPI](https://pypi.org/project/PyQt5/)

[Qt-Material — Qt Material documentation](https://qt-material.readthedocs.io/en/latest/index.html)

[PyInstaller Manual — PyInstaller 5.6.2 documentation](https://pyinstaller.org/en/stable/)

[auto-py-to-exe · PyPI](https://pypi.org/project/auto-py-to-exe/)
