'''
使用PYQT5作为gui
包括功能如下
开启识别
关闭识别
绑定快捷键(自动保存)
从其它文件中加载
关闭程序
'''
# from threading import Thread
from PyQt5 import QtGui
from key.waiting import binds,reloads
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel,QPushButton,QHBoxLayout,QLineEdit
from PyQt5.QtWidgets import QMessageBox
from GlobalStates import MyGlobalStates,resource_path
# import keyboard
from recognition.recognition import recognizer
from key.waiting import start_in_thread


from PyQt5.QtCore import pyqtSignal,Qt

class MyLineEdit(QLineEdit):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button()==Qt.LeftButton:
            self.clicked.emit()

# self.ges_dict = {0: 'cool', 1: 'eight', 2: 'fist', 3: 'five',
#                  4: 'four', 5: 'fuck', 6: 'nine', 7: 'one', 8: 'seven',
#                  9: 'six', 10: 'three', 11: 'two'
class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.set_UI()
        self.set_callbacks()

    def set_UI(self):
        self.setWindowTitle("Hot-Key-With-Hands-Recognition-V0.1")
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
        self.click_btns=[]
        self.edits=[]
        self.labels=[]

        l1=QLabel('one')
        l2=QLabel('two')
        l3=QLabel('three')
        l4=QLabel('four')
        l5=QLabel('five')
        l6=QLabel('six')
        l7=QLabel('seven')
        l8=QLabel('eight')
        l9=QLabel('nine')
        lfi=QLabel('fist')
        lfu=QLabel('fuck')
        lc=QLabel('cool')

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

        _one=  MyLineEdit(binds['one'])
        _two = MyLineEdit(binds['two'])
        _three = MyLineEdit(binds['three'])
        _four = MyLineEdit(binds['four'])
        _five = MyLineEdit(binds['five'])
        _six = MyLineEdit(binds['six'])
        _seven= MyLineEdit(binds['seven'])
        _eight = MyLineEdit(binds['eight'])
        _nine= MyLineEdit(binds['nine'])
        _fist = MyLineEdit(binds['fist'])
        _fuck = MyLineEdit(binds['fuck'])
        _cool = MyLineEdit(binds['cool'])

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

        # for e in self.edits:
        #     e.setFocusProxy(Qt.NoFocus)

        for i in range(len(binds.keys())):
            vlayout = QHBoxLayout()

            btn=QPushButton('Save')

            self.click_btns.append(btn)
            # PATH = QLineEdit(self.edits[i])
            # PATH.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑

            vlayout.addWidget(self.labels[i])
            vlayout.addWidget(self.edits[i])
            fromlayout.addRow(btn,vlayout)

        self.setLayout(fromlayout)
        MyGlobalStates.__run__ = False

    def set_callbacks(self):
        #绑定开始和结束按钮的按键,按下后修改全局状态标志位,修改开关状态的标签
        self.btn_start.clicked.connect(self.btn_start_callback)#这里差了一个回调函数
        self.btn_end.clicked.connect(self.btn_end_callback)

        # for i in range(len(self.edits)):
            # self.edits[i].clicked.connect(lambda: self.show_edits_change(i))
            # eval(f"self.edits[{i}].clicked.connect(lambda :self.show_edits_change({i}))")
        # self.edits[0].clicked.connect(lambda: self.show_edits_change(0))
        # self.edits[1].clicked.connect(lambda: self.show_edits_change(1))
        # self.edits[2].clicked.connect(lambda: self.show_edits_change(2))
        # self.edits[3].clicked.connect(lambda: self.show_edits_change(3))
        # self.edits[4].clicked.connect(lambda: self.show_edits_change(4))
        # self.edits[5].clicked.connect(lambda: self.show_edits_change(5))
        # self.edits[6].clicked.connect(lambda: self.show_edits_change(6))
        # self.edits[7].clicked.connect(lambda: self.show_edits_change(7))
        # self.edits[8].clicked.connect(lambda: self.show_edits_change(8))
        # self.edits[9].clicked.connect(lambda: self.show_edits_change(9))
        # self.edits[10].clicked.connect(lambda: self.show_edits_change(10))
        # self.edits[11].clicked.connect(lambda: self.show_edits_change(11))
        #
        self.edits[0].textChanged.connect(lambda: self.show_edits_change(0))
        self.edits[1].textChanged.connect(lambda: self.show_edits_change(1))
        self.edits[2].textChanged.connect(lambda: self.show_edits_change(2))
        self.edits[3].textChanged.connect(lambda: self.show_edits_change(3))
        self.edits[4].textChanged.connect(lambda: self.show_edits_change(4))
        self.edits[5].textChanged.connect(lambda: self.show_edits_change(5))
        self.edits[6].textChanged.connect(lambda: self.show_edits_change(6))
        self.edits[7].textChanged.connect(lambda: self.show_edits_change(7))
        self.edits[8].textChanged.connect(lambda: self.show_edits_change(8))
        self.edits[9].textChanged.connect(lambda: self.show_edits_change(9))
        self.edits[10].textChanged.connect(lambda: self.show_edits_change(10))
        self.edits[11].textChanged.connect(lambda: self.show_edits_change(11))

        for btn in self.click_btns:
            btn.clicked.connect(self.save_binds_and_reload)

    def btn_start_callback(self):
        if MyGlobalStates.__run__ == False:
            try:
                self.state.setText('On')
                MyGlobalStates.__run__=True
                recognizer.start_in_thread()
                start_in_thread()
            except Exception as e:
                QMessageBox.information(self, 'Error', e, QMessageBox.Ok)

    def btn_end_callback(self):
        self.state.setText('Close')
        MyGlobalStates.__run__=False

    def show_edits_change(self,idx):
        binds[list(binds.keys())[idx]]=self.edits[idx].text()

    def save_binds_and_reload(self):
        with open(resource_path('assets/bind.yml'),'w',encoding='utf-8') as f:
            f.write("#ALL_Gesture: {0: 'cool', 1: 'eight', 2: 'fist', 3: 'five', 4: 'four', 5: 'fuck', 6: 'nine', 7: 'one', 8: 'seven', 9: 'six', 10: 'three', 11: 'two'}\n")
            #保存配置
            for k in binds.keys():
                f.write(f"{k}: {binds[k]}\n")
            f.close()
        reloads()
        QMessageBox.information(self, 'Saving Changes', 'Saved Successfully !', QMessageBox.Ok)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        MyGlobalStates.__run__=False

'''
在主线程中打开
'''
def start_gui():
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())


