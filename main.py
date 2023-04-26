from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QMainWindow
from gesture_recognition_camera_ui import GestureControlUI
from shortcuts_setting_ui import ShortcutSettingUI
from translate_layer import TranslateMenuBar
from qt_material import apply_stylesheet
from file_resource_management import FileResources


class MainWindow(QWidget):
    switch_page_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.gesture_control_ui = GestureControlUI()
        self.settings_window = ShortcutSettingUI()
        self.stacked_widget.addWidget(self.gesture_control_ui)
        self.stacked_widget.addWidget(self.settings_window)
        self.gesture_control_ui.switch_page_signal.connect(self.switch_page)
        self.settings_window.switch_page_signal.connect(self.switch_page)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)
        self.resize(self.gesture_control_ui.sizeHint())

    def switch_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
        self.switch_page_signal.emit()


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(FileResources.get_APP_Icon())
        self.setWindowTitle('Gesture Recognition APP')
        self.main_window = MainWindow()
        self.setCentralWidget(self.main_window)
        self.translate_menu_bar = TranslateMenuBar()
        self.setMenuBar(self.translate_menu_bar)
        self.main_window.switch_page_signal.connect(self.switch_page)
        self.translate_menu_bar.language_changed_signal.connect(self.main_window.gesture_control_ui.set_all_texts)
        self.translate_menu_bar.language_changed_signal.connect(self.main_window.settings_window.set_all_texts)
        self.resize(self.main_window.stacked_widget.currentWidget().sizeHint())
    def switch_page(self):
        self.resize(self.main_window.stacked_widget.currentWidget().sizeHint())

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, theme='dark_teal.xml')
    # apply_stylesheet(app, theme='dark_purple.xml')
    app_window = AppWindow()
    app_window.show()
    app.exec_()