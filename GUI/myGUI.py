'''
使用PYQT5作为gui
包括功能如下
开启识别
关闭识别
绑定快捷键(自动保存)
从其它文件中加载
关闭程序
'''

from PyQt5 import QtGui
from key.waiting import binds,reloads
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel,QPushButton,QHBoxLayout,QLineEdit
from PyQt5.QtWidgets import QMessageBox
from GlobalStates import MyGlobalStates,resource_path

from recognition.recognition import recognizer
from key.waiting import start_in_thread

from qt_material import apply_stylesheet
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import pyqtSignal,Qt

class MyLineEdit(QLineEdit):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button()==Qt.LeftButton:
            self.clicked.emit()


class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.set_UI()
        self.set_callbacks()

    def set_UI(self):
        self.setWindowTitle("手势识别快捷键APP_V1.0")
        self.setWindowIcon(QIcon(resource_path(r'assets/1.ico')))
        # self.resize(400, 100)
        hlayout = QHBoxLayout()
        fromlayout = QFormLayout()

        self.state_label = QLabel('当前状态')
        self.state = QLabel(' 关闭')
        self.btn_start = QPushButton('开启手势识别')
        self.btn_end = QPushButton('关闭手势识别')

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



        for i in range(len(binds.keys())):
            vlayout = QHBoxLayout()

            btn=QPushButton('修改')

            self.click_btns.append(btn)


            vlayout.addWidget(self.labels[i])
            vlayout.addWidget(self.edits[i])
            fromlayout.addRow(btn,vlayout)

        self.setLayout(fromlayout)
        MyGlobalStates.__run__ = False

    def set_callbacks(self):
        #绑定开始和结束按钮的按键,按下后修改全局状态标志位,修改开关状态的标签
        self.btn_start.clicked.connect(self.btn_start_callback)#这里差了一个回调函数
        self.btn_end.clicked.connect(self.btn_end_callback)

        # It seems that this should work, however the `i` puts into the function is always 11
        # for i in range(len(self.edits)):
        #     self.edits[i].clicked.connect(lambda: self.edits_change_callback(i))
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
                self.state.setText('开启')
                MyGlobalStates.__run__=True
                recognizer.start_in_thread()
                start_in_thread()
            except Exception as e:
                QMessageBox.information(self, '异常', e, QMessageBox.Ok)

    def btn_end_callback(self):
        self.state.setText('关闭')
        MyGlobalStates.__run__=False

    def edits_change_callback(self, idx):
        binds[list(binds.keys())[idx]]=self.edits[idx].text()

    def save_binds_and_reload(self):
        with open(resource_path('assets/bind.yml'),'w',encoding='utf-8') as f:
            f.write("#所有能识别出来的手势: {0: 'cool', 1: 'eight', 2: 'fist', 3: 'five', 4: 'four', 5: 'fuck', 6: 'nine', 7: 'one', 8: 'seven', 9: 'six', 10: 'three', 11: 'two'}\n")
            #保存配置
            for k in binds.keys():
                f.write(f"{k}: {binds[k]}\n")
            f.close()
        reloads()
        QMessageBox.information(self, '修改按键', '按键绑定修改成功', QMessageBox.Ok)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        MyGlobalStates.__run__=False

'''
在主线程中打开
'''
def start_gui():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    form = Winform()
    form.show()
    sys.exit(app.exec_())


