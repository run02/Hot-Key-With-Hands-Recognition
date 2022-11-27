'''
要训练的模型放在GestureVideos,
目录一共有两级,第一层建一堆文件夹,文件夹的名字就是手势的名字
文件夹下可以放很多视频,会根据这些视频生成训练用的矩阵
这个函数的作用是建立一个二维列表
第一维是每一个文件夹的名称,
第二维是每一个文件夹下每一个视频的路径
返回这个二维列表,下一步用cv2分别打开就能生成训练集了
'''
import os
from GlobalStates import resource_path
import numpy as np
import cv2
import mediapipe as mp
def load_paths()->dict:
    gestures_root = resource_path('GestureVideos')
    labels = []
    gestures_dir = []
    for each_gesture in os.listdir(gestures_root):
        labels.append(each_gesture)
        gestures_dir.append(os.path.join(gestures_root, each_gesture))

    videos_dict = {}
    for i in range(len(gestures_dir)):
        dir = gestures_dir[i]
        label = labels[i]
        videos_dict[label] = []
        for vedio in os.listdir(dir):
            videos_dict[label].append(os.path.join(dir, vedio))
    np.save(os.path.join(resource_path('DataForTraining'),'all_gestures.npy'),list(videos_dict.keys()))
    return videos_dict

# '''
# 生成训练集比较耗时,
# 这里搞一个保存生成训练集进度的函数,方便断点续训
# 会在DataForTraining目录下生成一个`progress.npy`文件
# 这样下次只需要按照这个加载就行了
# '''
# progress1=resource_path('DataForTraining/progress1.npy')
# def save_progress(label,vedio):
#     np.save(progress1,[label,vedio])
#
# def load_progress():
#     try:
#         p=np.load(progress1, allow_pickle=True).tolist()
#         return p
#     except FileNotFoundError:
#         return [None,None]
#
# '''
# 使用cv2播放视频,放入mediapipe中训练
# 每训练完成一个视频就把矩阵保存到`DataForTraining目录下`,
# 同时给视频按照文件夹名称打上标签
# '''



seve_matrix=resource_path('DataForTraining')
def generate_training_sets(show_img=True):
    mp_drawing = mp.solutions.drawing_utils  # 创建一个绘图工具
    mp_drawing_styles = mp.solutions.drawing_styles  # 创建一个绘图样式
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(model_complexity=0, min_detection_confidence=0.8, min_tracking_confidence=0.8)

    global seve_matrix
    videos_dict=load_paths()#加载每个标签下的每个视频
    # if last_label is not None:

    for label in videos_dict.keys():
         #列表里放的是每个视频训练出的列表,
        if videos_dict[label] !=[]:
            training_x_list = []
            for vedio in videos_dict[label]:
                print(vedio)
                training_x=[] #每个视频加载出的训练集
                cap = cv2.VideoCapture(vedio)
                while (cap.isOpened()):
                    success, image = cap.read()
                    if success:
                        image = cv2.flip(image, 1)
                        # 将图片设置为不可写，提升性能
                        image.flags.writeable = False
                        # 转换为RGB格式
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        # 调用mediapipe框架读取特征点，特征点为1个对象，保存在results中
                        results = hands.process(image)
                        # 打开图像可写的开关，将颜色由RGB转化成BGR,加速
                        image.flags.writeable = True
                        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                        if results.multi_hand_world_landmarks:
                            # print(len(results.multi_hand_landmarks))
                            hand_landmarks = results.multi_hand_landmarks[0]
                            landmark21 = []
                            for landmark in hand_landmarks.landmark:
                                x = landmark.x
                                y = landmark.y
                                z = landmark.z
                                landmark21.append((x, y, z))
                            # landmark21_ = np.array(landmark21)
                            training_x.append(landmark21)

                            if show_img:
                                l=results.multi_handedness[0]
                                # print()
                                cv2.putText(image, str(l.classification[0].label), (100, 200), 0, 1.3, (0, 0, 255), 3)
                                # print(results.multi_handedness)
                                cv2.putText(image, str(label), (0, 100), 0, 1.3, (0, 0, 255), 3)
                                # 将手部的特征点连线显示
                                for hand_landmarks in results.multi_hand_landmarks:
                                   mp_drawing.draw_landmarks(
                                        image,
                                        hand_landmarks,
                                        mp_hands.HAND_CONNECTIONS,
                                        mp_drawing_styles.get_default_hand_landmarks_style(),
                                        mp_drawing_styles.get_default_hand_connections_style())
                        cv2.imshow('Gesture Training', image)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    else:
                        cap.release()
                        cv2.destroyAllWindows()


                cap.release()
                cv2.destroyAllWindows()
                training_x_list.append(training_x)

            np.save(os.path.join(seve_matrix,label+'.npy'),training_x_list)
    return "ok"




