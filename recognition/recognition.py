'''
运行该程序进行手势识别,
摄像头可以来自于本地摄像头,也可以来自于udp视频透传
手术识别完成后可根据识别出的手势发送控制
最好作为主线程运行
'''
import cv2
import mediapipe as mp
from threading import Thread
try:
    import tensorflow.python.keras as keras
except:
    import tensorflow.keras as keras
import numpy as np
from GlobalStates import MyGlobalStates

'''
提供手势识别的类
访问 .now_ges 获得现阶段的手势名称
'''

class My_indentify():
    def __init__(self):
        # self.ges_dict = np.load('assets/num_to_ss.npy', allow_pickle=True) #识别出来的手势是数字,需要用字典把序号转化成字符串,加载保存的对照表
        # self.ges_dict = self.ges_dict.tolist()
        self.ges_dict = {0: 'cool', 1: 'eight', 2: 'fist', 3: 'five', 4: 'four', 5: 'fuck', 6: 'nine', 7: 'one', 8: 'seven', 9: 'six', 10: 'three', 11: 'two'}
        print(self.ges_dict)
        self.my_model = keras.models.load_model('assets/my_train_12_gestures2')  # 加载训练好的tensorflow模型
        self.mp_drawing = mp.solutions.drawing_utils  # 创建一个绘图工具
        self.mp_drawing_styles = mp.solutions.drawing_styles  # 创建一个绘图样式
        self.mp_hands = mp.solutions.hands  # 创建mediapipe框架读取特征点的初步工具，需要输入一个视频流，后通过自定义的tenslrflow神经网络获得手势预测值
        self.hands = self.mp_hands.Hands(model_complexity=0, min_detection_confidence=0.8, min_tracking_confidence=0.8)
        self.now_ges = 'none' #用于共享出去,给其他程序获得手势的标志位
        self.pre = []  # tensorflow模型预测输出为一个包含12个权值的list



    def start_in_loop(self,show_img=True):
        self.cap=cv2.VideoCapture(0)
        while True:
            if MyGlobalStates.__run__ is True:
                # time.sleep(0.05)
                # 从摄像头读一帧画面
                success, image = self.cap.read()
                if success:
                    image = cv2.flip(image, 1)
                    # 将图片设置为不可写，提升性能
                    image.flags.writeable = False
                    # 转换为RGB格式
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    # 调用mediapipe框架读取特征点，特征点为1个对象，保存在results中
                    results = self.hands.process(image)
                    # 打开图像可写的开关，将颜色由RGB转化成BGR,加速
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    # 获取手势预测值
                    # 遍历results变量中的结果，将结果转化为nmupy数组格式输入神经网络进行预测

                    if results.multi_hand_landmarks:
                        # print(len(results.multi_hand_landmarks))
                        for hand_landmarks in results.multi_hand_landmarks:
                            landmark21 = []
                            for i in range(21):
                                x = hand_landmarks.landmark[i].x
                                y = hand_landmarks.landmark[i].y
                                z = hand_landmarks.landmark[i].z
                                landmark21.append((x, y, z))
                            landmark21_ = np.array([landmark21])
                            # 输入神经网络进行预测，得到预测结果为每一种手势对应的概率
                            pre = self.my_model.predict(landmark21_[:1])
                            # 预测结果大于0.5认为结果可信，进入下一步判断，可更改该值获得更高或较低的可信度
                            if np.max(pre) > 0.5:
                                # 得到预测结概率最大的手势的编号
                                ges_pre_p = np.argmax(pre)
                                # 将手势编号通过字典转化为我们给他起名的字符串
                                self.now_ges = self.ges_dict[ges_pre_p]
                        # 显示我们预测的手势与概率
                        if show_img:
                            cv2.putText(image, str(np.max(pre)), (100, 200), 0, 1.3, (0, 0, 255), 3)
                            cv2.putText(image, self.now_ges, (0, 100), 0, 1.3, (0, 0, 255), 3)
                            # 将手部的特征点连线显示
                            for hand_landmarks in results.multi_hand_landmarks:
                                self.mp_drawing.draw_landmarks(
                                    image,
                                    hand_landmarks,
                                    self.mp_hands.HAND_CONNECTIONS,
                                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                                    self.mp_drawing_styles.get_default_hand_connections_style())
                    else:
                        self.now_ges='none'
                    if show_img:
                        cv2.namedWindow('Gesture Recognition Client', cv2.WINDOW_NORMAL)
                        # 展示图片画面
                        cv2.imshow('Gesture Recognition Client', image)
                        # 按esc键退出
                        if cv2.waitKey(5) & 0xFF == 27:
                            break
            else:
                break
        self.free()
    def free(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def start_in_thread(self):
        Thread(target=self.start_in_loop).start()#,name='recognizer')


recognizer=My_indentify()
# recognizer.start_in_thread()

