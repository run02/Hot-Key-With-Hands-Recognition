import os
import sys
import yaml
from PyQt5.QtGui import QIcon
from tensorflow.python.keras.models import load_model

from abstract_layer import FileResourceManagementInterface


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


GESTURES2SHORTCUTS_PATH = 'assets/gestures2shortcuts.yml'
AI_MODEL_PATH = 'assets/saved_ai_model'
TRANSLATIONS_PATH = 'assets/translations.yml'
APP_ICON_PATH = 'assets/APPICO.ico'
MESSAGE_BOX_ICON_PATH = 'assets/MessageBox.ico'
MESSAGE_BOX_OK_ICON_PATH = 'assets/Message_OK.ico'
GESTURES_ICONS_PATH = 'assets/gestures_icons/'


def load_qss(relative_path):
    with open(resource_path(relative_path), 'r', encoding='utf-8') as f:
        qss = f.read()
    return qss


class FileResourceManagement(FileResourceManagementInterface):
    def __init__(self):
        self.gestures2shortcuts = self.load_gestures2shortcuts_dictionary(GESTURES2SHORTCUTS_PATH)
        self.load_ai_modules(AI_MODEL_PATH)
        self.translations = self.load_translations(TRANSLATIONS_PATH)

    def load_gestures2shortcuts_dictionary(self, relative_path):
        with open(resource_path(relative_path), 'r', encoding='utf-8') as f:
            d = yaml.load(f.read(), Loader=yaml.FullLoader)
            f.close()
        return d

    def load_translations(self, relative_path=TRANSLATIONS_PATH):
        with open(resource_path(relative_path), "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def update_dictionary(self, key, value):
        self.gestures2shortcuts[key] = value

    def backup_dictionary(self, relative_path=GESTURES2SHORTCUTS_PATH):
        with open(resource_path(relative_path), "w", encoding="utf-8") as yaml_file:
            yaml.dump(self.gestures2shortcuts, yaml_file, allow_unicode=True)
            yaml_file.close()

    def import_key_value_file(self, file_path):
        pass

    def load_ai_modules(self, relative_path):
        self.ai_model = load_model(resource_path(relative_path))  # 加载训练好的tensorflow模型

    def get_APP_Icon(self):
        return QIcon(resource_path(APP_ICON_PATH))

    def get_MessageBoxIcon(self):
        return QIcon(resource_path(MESSAGE_BOX_ICON_PATH))

    def get_MessageBoxOKIcon(self):
        return QIcon(resource_path(MESSAGE_BOX_OK_ICON_PATH))

    def get_gestures_icons_path_by_key(self, key):
        return resource_path(f"{GESTURES_ICONS_PATH}/{key}.ico")

    def load_gesture_control_qss(self):
        return load_qss('assets/styles/gesture_control_ui.qss')

    def load_shortcuts_setting_qss(self):
        return load_qss('assets/styles/shortcut_setting_ui.qss')

    def load_menubar_qss(self):
        return load_qss('assets/styles/menuBar.qss')


FileResources = FileResourceManagement()
