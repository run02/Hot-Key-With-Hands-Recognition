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
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel,QPushButton,QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from GlobalStates import MyGlobalStates
import keyboard
from recognition.recognition import recognizer
from key.waiting import start_in_thread

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.set_UI()
        self.set_callbacks()

    def set_UI(self):
        self.setWindowTitle("手势识别快捷键APP_V1.0")
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

        for k in binds.keys():
            vlayout = QHBoxLayout()
            labl = QLabel(k)
            lineEdit =QPushButton(binds[k])
            lineEdit.setMinimumWidth(30)
            # lineEdit.setMaximumWidth(30)
            btn=QPushButton('确定')

            self.click_btns.append(btn)
            self.edits.append(lineEdit)

            vlayout.addWidget(labl)
            vlayout.addWidget(lineEdit)
            fromlayout.addRow(btn,vlayout)

        self.setLayout(fromlayout)
        MyGlobalStates.__run__ = False

    def set_callbacks(self):
        #绑定开始和结束按钮的按键,按下后修改全局状态标志位,修改开关状态的标签
        self.btn_start.clicked.connect(self.btn_start_callback)#这里差了一个回调函数
        self.btn_end.clicked.connect(self.btn_end_callback)

        # for edit in self.edits:
        #     edit.clicked.connect(lambda:self.show_edits_change(edit))


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

    def show_edits_change(self,edit:QPushButton):
        k=keyboard.read_hotkey()
        idx=self.edits.index(edit)
        print(list(binds.keys())[idx])
        # print(l[idx])
        # binds[binds.keys()[idx]]=k
        edit.setText(k)


    def save_binds_and_reload(self):
        with open('assets/bind.yml','w',encoding='utf-8') as f:
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
    form = Winform()
    form.show()
    sys.exit(app.exec_())


