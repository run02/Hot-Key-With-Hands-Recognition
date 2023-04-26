from PyQt5.QtWidgets import QPushButton, QLabel, QMenuBar, QCheckBox, QMessageBox
from file_resource_management import FileResources
from PyQt5.QtWidgets import QActionGroup, QAction, QMenu
from PyQt5.QtCore import pyqtSignal

global_translations = FileResources.load_translations()["translations"]
global_languages = FileResources.load_translations()["supported_languages"]
global_lang = global_languages[0]


def get_translation(key, lang, translations):
    if key in translations:
        if lang in translations[key]:
            return translations[key][lang]
        else:
            print(f"Language '{lang}' not found for key '{key}'.")
            return key
    else:
        print(f"Key '{key}' not found.")
        return key


class TranslatedButton(QPushButton):
    def setText(self, key):
        self.key = key
        text = get_translation(key, global_lang, global_translations)
        super().setText(text)


class TranslatedLabel(QLabel):
    def setText(self, key, second=None):
        self.key = key
        text = get_translation(key, global_lang, global_translations)
        if second is not None:
            text = text + ": " + second
        super().setText(text)


class TranslatedCheckBox(QCheckBox):
    def setText(self, key):
        self.key = key
        text = get_translation(key, global_lang, global_translations)
        super().setText(text)


class TranslateMessageBox(QMessageBox):
    def setText(self, key):
        self.key = key
        text = get_translation(key, global_lang, global_translations)
        super().setText(text)

    def setWindowTitle(self, title):
        self.title = title
        text = get_translation(title, global_lang, global_translations)
        super().setWindowTitle(text)


class TranslateMenuBar(QMenuBar):
    language_changed_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(FileResources.load_menubar_qss())
        self.init_menu_bar()

    def init_menu_bar(self):
        self.language_menu = QMenu(get_translation("Language", global_lang, global_translations), self)
        self.addMenu(self.language_menu)

        language_group = QActionGroup(self)
        language_group.setExclusive(True)

        for lang_name in global_languages:
            language_action = QAction(lang_name, self, checkable=True)
            language_action.triggered.connect(
                lambda checked, l=lang_name: self.on_language_changed(l) if checked else None)
            self.language_menu.addAction(language_action)
            language_group.addAction(language_action)

        self.language_menu.actions()[0].setChecked(True)

    def on_language_changed(self, lang):
        global global_lang
        global_lang = lang
        self.language_menu.setTitle(get_translation("Language", global_lang, global_translations))
        self.language_changed_signal.emit(lang)

# if __name__ == "__main__":
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow,
#     app = QApplication([])
#     window = QMainWindow()
#     translateMenuBar = TranslateMenuBar()
#     window.setMenuBar(translateMenuBar)
#     window.show()
#     sys.exit(app.exec_())
