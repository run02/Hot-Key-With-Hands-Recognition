import sys
import os

#When packing to an .exe app in one file, we need this to fix the `file not find error` , Otherwise it will not be affected
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# When MyGlobalStates.__run__=False, all  child-threads will quit
class MyGlobalStates():
    __run__: bool=False
