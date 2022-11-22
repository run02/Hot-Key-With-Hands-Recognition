import time
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

print(resource_path(r'assets\bind.yml'))
# import keyboard
#
#
# print(keyboard.read_hotkey())
# keyboard.press('a+b+c')
# import threading
#
# import requests
# def test():
#     while True:
#         a=requests.get('http://42.192.227.238/DianDongChe_people/all_people')
#         print(a.text)
#         b=eval(a.text)[0]
#         print(b['company_name'])
#         time.sleep(2)
#
# threading.Thread(target=test).start()
# while  True:
#     print(123)
#     time.sleep(2)
# d={'one': 's', 'nine': 's', 'five': 'x', 'six': 'z', 'eight': 'w', 'three': 'space'}
# print(d.keys())
# print(d.keys())
# print()
# print(type(d.keys()))
#
