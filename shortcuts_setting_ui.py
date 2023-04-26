from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QToolButton, QScrollArea, QSizePolicy
from translate_layer import TranslatedButton as QPushButton,TranslatedLabel as QLabel,TranslateMessageBox as QMessageBox
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import QLineEdit
from file_resource_management import FileResources
from abstract_layer import Gesture_Control_PAGE



class KeyCaptureLineEdit(QLineEdit):
    key_pressed = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(KeyCaptureLineEdit, self).__init__(*args, **kwargs)
        self.setReadOnly(True)

    def keyPressEvent(self, event):
        key = event.key()
        modifiers = int(event.modifiers())
        key_combo = QKeySequence(modifiers | key).toString()
        self.setText(key_combo)
        self.key_pressed.emit(key_combo)
        super(KeyCaptureLineEdit, self).keyPressEvent(event)


class ShortcutSettingUI(QWidget):
    switch_page_signal = pyqtSignal(int)

    def __init__(self, parent=None):
        super(ShortcutSettingUI, self).__init__(parent)
        self.setStyleSheet(FileResources.load_shortcuts_setting_qss())
        self.init_ui()
        self.set_callbacks()
    def set_widgets(self):
        self.back_button = QPushButton()
        self.confirm_button = QPushButton()


    def set_all_texts(self):
        self.back_button.setText("Return")
        self.confirm_button.setText("Modify")

    def init_ui(self):
        self.set_widgets()
        self.set_all_texts()

        layout = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_layout.setSpacing(10)  # Add spacing between layouts in scroll_layout

        key_value_pairs = FileResources.gestures2shortcuts
        for key, value in key_value_pairs.items():

            icon = QIcon(FileResources.get_gestures_icons_path_by_key(key))

            tool_button = QPushButton()

            tool_button.setIcon(icon)
            tool_button.setIconSize(QSize(150,150))
            tool_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            tool_button.setFixedSize(QSize(151, 151))

            line_edit = KeyCaptureLineEdit()

            line_edit.setText(value)
            line_edit.key_pressed.connect(lambda key_combo, k=key: self.on_key_pressed(k, key_combo))

            sub_layout = QHBoxLayout()


            sub_layout.addWidget(tool_button,1)
            sub_layout.addWidget(line_edit,1)

            scroll_layout.addLayout(sub_layout)

        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area)

        bh = QHBoxLayout()
        bh.setSpacing(10)
        bh.addWidget(self.back_button)
        bh.addWidget(self.confirm_button)
        layout.addLayout(bh)
        self.setLayout(layout)

    def set_callbacks(self):
        self.back_button.clicked.connect(self.go_back_callback)
        self.confirm_button.clicked.connect(self.confirm_button_callback)

    def go_back_callback(self):
        self.switch_page_signal.emit(Gesture_Control_PAGE)

    def on_key_pressed(self, key, key_combo):
        FileResources.update_dictionary(key, key_combo)


    def confirm_button_callback(self):
        FileResources.backup_dictionary()
        msg_box = QMessageBox()
        # 设置提示框标题和信息
        msg_box.setWindowTitle("Modify Confirm")
        msg_box.setWindowIcon(FileResources.get_MessageBoxIcon())
        msg_box.setIconPixmap(FileResources.get_MessageBoxOKIcon().pixmap(48, 48))
        msg_box.setText("Shortcuts Modified!")
        msg_box.exec_()

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     editor = ShortcutSettingUI()
#     editor.show()
#     sys.exit(app.exec_())
