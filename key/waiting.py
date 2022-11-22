from recognition.recognition import recognizer
import keyboard
import yaml #读配置文件的
import time
from threading import Thread
from GlobalStates import MyGlobalStates
def load(file="assets/bind.yml")->dict:
    with open(file, 'r', encoding='utf-8') as f:
        binds = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    return binds


binds=load()
print("当前按键绑定情况: ")
print(binds)

def reloads():
    global binds
    binds=load()


def waiting_to_press_and_release():
    global binds
    while True:
        if MyGlobalStates.__run__:
            if recognizer.now_ges in binds.keys():
                if binds[recognizer.now_ges]!='nothing':
                    keyboard.press_and_release(binds[recognizer.now_ges])
            time.sleep(0.2)
        else:
            break

#等待开启的线程
def start_in_thread():
    Thread(target=waiting_to_press_and_release).start()

