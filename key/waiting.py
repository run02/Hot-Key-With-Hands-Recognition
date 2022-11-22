from recognition.recognition import recognizer
import keyboard
import yaml #读配置文件的
import time
from threading import Thread
from GlobalStates import MyGlobalStates,resource_path

def load(file=resource_path("assets/bind.yml"))->dict:
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

# _buffer=['none','none']
# def push_buffer(new:str):
#     _buffer[0]=_buffer[1]
#     _buffer[1]=new
#
# def buffer_diff()->bool:
#     return _buffer[0]==_buffer[1]


def waiting_to_press_and_release():
    global binds
    while True:
        if MyGlobalStates.__run__:
            if recognizer.now_ges in binds.keys():
                # push_buffer(recognizer.now_ges)
                if binds[recognizer.now_ges]!='nothing' :
                    keyboard.press_and_release(binds[recognizer.now_ges])
            time.sleep(0.35)
        else:
            break

#等待开启的线程
def start_in_thread():
    Thread(target=waiting_to_press_and_release).start()

