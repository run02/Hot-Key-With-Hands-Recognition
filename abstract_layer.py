'''
You can implement gesture recognition and shortcut key triggering functionality
with a different model based on the interface format provided by the abstraction layer
This version is not yet fully developed, the complete abstraction of the upper-layer interface
may be implemented in the next version

可以根据抽象层提供的接口格式用另外的模型实现手势识别触发快捷键的功能,这一版本还不健全, 上层接口完整的抽象可能会在下一版本实现
'''

from abc import ABC, abstractmethod

page_switch = 0
Gesture_Control_PAGE = 0
KeyCaptureLineEdit_PAGE = 1


class ShortcutLayerInterface(ABC):
    '''
    This layer is responsible for triggering pre-defined shortcut keys based on gestures
    这一层负责根据手势触发设置好的快捷键
    '''

    @abstractmethod
    def trigger_shortcut(self, key):
        '''
        Press the specified shortcut key or combination shortcut key.
        按下指定快捷键或组合快捷键
        :param key:
                   combination shortcut key
                   组合快捷键
        '''
        pass


class FileResourceManagementInterface(ABC):
    '''
    This layer is responsible for load all kinds of icons, qss style sheets, config files and so on,
    also responsible for saving the config files.
    The layers above this layer do not need to repeat inputting various paths for ease of maintenance.

    这一层负责加载各种图标,qss样式,配置文件等, 以及配置文件的保存
    目的是在这一层提供所有的资源的加载与保存, 在这一层之上的层不用重复出现路径,方便维护
    '''

    @abstractmethod
    def load_gestures2shortcuts_dictionary(self, relative_path):
        pass

    @abstractmethod
    def update_dictionary(self, key, value):
        pass

    @abstractmethod
    def backup_dictionary(self):
        pass

    @abstractmethod
    def import_key_value_file(self, file_path):
        pass

    @abstractmethod
    def load_ai_modules(self, relative_path):
        pass


class GestureRecognitionCameraInterface(ABC):
    '''
    This layer provides camera and gesture recognition functionality,
    as well as display the camera inter face and managing resource allocation and recovery.
    To implement custom gesture recognition, you can use your own model and implement two methods.
    The recognized result must be put into the output queue, which will be periodically checked by
    the controller ui, To ensure real-time performance a queue with a length of 1 or
    another suitable data structure can be used.
    To make this UI system compatible with a custom model,
    modify the 'gestures2shortcuts.yml' file to recognize actions based on the model's output,
    and replace the pictures in the 'assets/gestures_icons' directory with custom images.

    这一层负责提供摄像头和手势识别,以及摄像头界面展示,摄像头资源调用与回收
    如果想要实现自定义的手势识别,可以使用自己的模型并实现两个方法,别忘了将识别出的结果放入输出队列
    主界面中将会定期查看队列中识别输出的结果, 如果需要保证是实时性, 可以用长度为1的队列或者是其它结构
    为了使这套UI适应自定义的模型,更改gestures2shortcuts.yml为模型识别的动作,
    再将assets/gestures_icons路径下的图片换为自定义的图片即可完成.
    '''

    @abstractmethod
    def process_images(self, start_event, stop_event, output_queue, show_image):
        '''
        This function runs a gesture recognition and signal sending model within a main loop
        using multiprocessing for improved performance.
        The recognized results should be put into the output queue.
        在大循环中运行一个手势识别与信号发送的模型,这里是使用multiprocessing的方式(提示性能)
        需要将识别出的结果放到output_queue中
        :param start_event:  signal for starting the loop 开始的信号
        :param stop_event:   signal for stopping the loop 结束的信号
        :param output_queue: for storing the recognized results 识别出来的结果
        :param show_image:   for displaying camera content if desired 是否展示摄像头内容
        '''
        pass

    @abstractmethod
    def free(self):
        pass

    @abstractmethod
    def recognize_gesture(self, frame) -> str:
        '''
        This function recognizes the name of the gesture based on the camera image.
        :param frame: camera image 摄像头画面
        :return: recognized gesture 手势名称
        '''
        pass

# '''
# The following code is related to the interface,
# and since ideas can change rapidly,
# it may not be easy to abstract them.
# The code below is a draft version.
# 以下是跟界面相关的, 想法的变化比较快, 暂时不太好抽象
# 下边是一个草稿版
# '''

# from PyQt5.QtCore import pyqtSignal
# class TranslateLayerInterface(ABC):
#     '''
#     Responsible for providing language selection and translation functionality
#     负责提供语言的选择和翻译
#     '''
#     language_changed_signal = pyqtSignal(str)
#     @abstractmethod
#     def on_language_changed(self, lang):
#     pass
# class GestureRecognitionCameraUIInterface(ABC):
#     '''
#     Responsible for controlling the GestureRecognitionCamera layer
#     负责操控GestureRecognitionCameraUI层
#     '''
#     switch_page_signal = pyqtSignal(int)
#     @abstractmethod
#     def set_all_texts(self):
#         '''
#         Rewrite all text settings in response to page switching
#         响应界面切换时重写设置文字
#         '''
#         pass
#     pass
# class ShortcutSettingUIInterface(ABC):
#     '''
#     Responsible for capturing shortcut keys, updating files, and providing relevant interfaces
#     负责捕捉快捷键以及更新文件,并提供相应的界面
#     '''
#     switch_page_signal = pyqtSignal(int)
#     @abstractmethod
#     def set_all_texts(self):
#     pass
#     pass
# class PyQtMainInterface(ABC):
#     '''
#     Responsible for loading the above interface modules and binding signals
#     负责加载上述界面的模块,绑定信号
#     '''
#     switch_page_signal = pyqtSignal()
#     pass