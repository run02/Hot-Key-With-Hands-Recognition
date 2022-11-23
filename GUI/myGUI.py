import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from qt_material import apply_stylesheet
from GlobalStates import MyGlobalStates, resource_path
from key.waiting import binds, reloads, start_in_thread
from recognition.recognition import recognizer


# UI and callbacks
class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.set_UI()
        self.set_callbacks()

    def set_UI(self):
        self.setWindowTitle("Hot-Key-With-Hands-Recognition-V0.1")
        self.setWindowIcon(QIcon(resource_path(r'assets/1.ico')))
        # self.resize(400, 100)
        hlayout = QHBoxLayout()
        fromlayout = QFormLayout()

        self.state_label = QLabel('Status')
        self.state = QLabel(' OFF')
        self.btn_start = QPushButton('Start')
        self.btn_end = QPushButton('Close')

        hlayout.addWidget(self.state_label)
        hlayout.addWidget(self.state)
        hlayout.addWidget(self.btn_start)
        hlayout.addWidget(self.btn_end)

        fromlayout.addRow(hlayout)
        self.click_btns = []
        self.edits = []
        self.labels = []

        l1 = QLabel('one')
        l2 = QLabel('two')
        l3 = QLabel('three')
        l4 = QLabel('four')
        l5 = QLabel('five')
        l6 = QLabel('six')
        l7 = QLabel('seven')
        l8 = QLabel('eight')
        l9 = QLabel('nine')
        lfi = QLabel('fist')
        lfu = QLabel('fuck')
        lc = QLabel('cool')

        self.labels.append(l1)
        self.labels.append(l2)
        self.labels.append(l3)
        self.labels.append(l4)
        self.labels.append(l5)
        self.labels.append(l6)
        self.labels.append(l7)
        self.labels.append(l8)
        self.labels.append(l9)
        self.labels.append(lfi)
        self.labels.append(lfu)
        self.labels.append(lc)

        _one = QLineEdit(binds['one'])
        _two = QLineEdit(binds['two'])
        _three = QLineEdit(binds['three'])
        _four = QLineEdit(binds['four'])
        _five = QLineEdit(binds['five'])
        _six = QLineEdit(binds['six'])
        _seven = QLineEdit(binds['seven'])
        _eight = QLineEdit(binds['eight'])
        _nine = QLineEdit(binds['nine'])
        _fist = QLineEdit(binds['fist'])
        _fuck = QLineEdit(binds['fuck'])
        _cool = QLineEdit(binds['cool'])

        self.edits.append(_one)
        self.edits.append(_two)
        self.edits.append(_three)
        self.edits.append(_four)
        self.edits.append(_five)
        self.edits.append(_six)
        self.edits.append(_seven)
        self.edits.append(_eight)
        self.edits.append(_nine)
        self.edits.append(_fist)
        self.edits.append(_fuck)
        self.edits.append(_cool)

        for i in range(len(binds.keys())):
            vlayout = QHBoxLayout()

            btn = QPushButton('Save')

            self.click_btns.append(btn)

            vlayout.addWidget(self.labels[i])
            vlayout.addWidget(self.edits[i])
            fromlayout.addRow(btn, vlayout)

        self.setLayout(fromlayout)
        MyGlobalStates.__run__ = False

    # bind all callbacks to Widgets
    def set_callbacks(self):
        self.btn_start.clicked.connect(self.btn_start_callback)
        self.btn_end.clicked.connect(self.btn_end_callback)

        # Code like this that It won't work, the `i` is always 11 when it calls the callback function
        # So I had to write it one by one
        # for i in range(len(self.edits)):
        #  self.edits[i].textChanged.connect(lambda: self.edits_change_callback(i))
        self.edits[0].textChanged.connect(lambda: self.edits_change_callback(0))
        self.edits[1].textChanged.connect(lambda: self.edits_change_callback(1))
        self.edits[2].textChanged.connect(lambda: self.edits_change_callback(2))
        self.edits[3].textChanged.connect(lambda: self.edits_change_callback(3))
        self.edits[4].textChanged.connect(lambda: self.edits_change_callback(4))
        self.edits[5].textChanged.connect(lambda: self.edits_change_callback(5))
        self.edits[6].textChanged.connect(lambda: self.edits_change_callback(6))
        self.edits[7].textChanged.connect(lambda: self.edits_change_callback(7))
        self.edits[8].textChanged.connect(lambda: self.edits_change_callback(8))
        self.edits[9].textChanged.connect(lambda: self.edits_change_callback(9))
        self.edits[10].textChanged.connect(lambda: self.edits_change_callback(10))
        self.edits[11].textChanged.connect(lambda: self.edits_change_callback(11))

        for btn in self.click_btns:
            btn.clicked.connect(self.save_binds_and_reload)

    def btn_start_callback(self):
        if MyGlobalStates.__run__ == False:
            try:
                self.state.setText('On')
                MyGlobalStates.__run__ = True
                recognizer.start_in_thread()
                start_in_thread()
            except Exception as e:
                QMessageBox.information(self, 'Error', str(e), QMessageBox.Ok)

    def btn_end_callback(self):
        self.state.setText('Close')
        MyGlobalStates.__run__ = False

    def edits_change_callback(self, idx):
        binds[list(binds.keys())[idx]] = self.edits[idx].text()

    # save changes,refresh the bindings for hotkey and gestures
    def save_binds_and_reload(self):
        with open(resource_path('assets/bind.yml'), 'w', encoding='utf-8') as f:

            for k in binds.keys():
                f.write(f"{k}: {binds[k]}\n")
            f.close()
        reloads()
        QMessageBox.information(self, 'Saving Changes', 'Saved Successfully !', QMessageBox.Ok)

    # When MyGlobalStates.__run__=False, all  child-threads will quit
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        MyGlobalStates.__run__ = False


# program entry
def start_gui():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    form = Winform()
    form.show()
    sys.exit(app.exec_())
