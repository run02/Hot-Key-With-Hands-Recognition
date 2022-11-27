'''
要训练的模型放在GestureVideos,
目录一共有两级,第一层建一堆文件夹,文件夹的名字就是手势的名字
文件夹下可以放很多视频,会根据这些视频生成训练用的矩阵
这个函数的作用是建立一个二维列表
第一维是每一个文件夹的名称,
第二维是每一个文件夹下每一个视频的路径
返回这个二维列表,下一步用cv2分别打开就能生成训练集了
'''
def load_paths()->list:

    return

'''
生成训练集比较耗时,
这里搞一个保存生成训练集进度的函数,方便断点续训
会在DataForTraining目录下生成一个`progress.npy`文件
这样下次只需要按照这个加载就行了
'''
def save_completion():

    return

'''
使用cv2播放视频,放入mediapipe中训练
每训练完成一个视频就把矩阵保存到`DataForTraining目录下`,
同时给视频按照文件夹名称打上标签
'''
def generate_training_sets(paths:list):
    return