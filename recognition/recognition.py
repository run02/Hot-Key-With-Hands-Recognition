import cv2
import mediapipe as mp
from threading import Thread

try:
    from tensorflow.python.keras.models import load_model
except ImportError:
    from tensorflow.keras.models import load_model

import numpy as np
from GlobalStates import MyGlobalStates, resource_path

'''
After calling the start_in_thread method,
Refresh the `now_ges` variable according to the recognition result,
External programs can get the current gesture by reading `now_ges` variable
'''


class My_indentify():
    def __init__(self):
        self._ges_dict = {0: 'cool', 1: 'eight', 2: 'fist', 3: 'five',
                          4: 'four', 5: 'fuck', 6: 'nine', 7: 'one', 8: 'seven',
                          9: 'six', 10: 'three', 11: 'two'}

        self._my_model = load_model(resource_path('assets/my_train_12_gestures2'))
        self._mp_drawing = mp.solutions.drawing_utils
        self._mp_drawing_styles = mp.solutions.drawing_styles
        self._mp_hands = mp.solutions.hands
        self._hands = self._mp_hands.Hands(model_complexity=0, min_detection_confidence=0.8,
                                           min_tracking_confidence=0.8)
        self.now_ges = 'none'  # shared with external programs
        self._pre = []

    def start_in_loop(self, show_img=True):
        self._cap = cv2.VideoCapture(0)
        while True:
            if MyGlobalStates.__run__ is True:

                success, image = self._cap.read()
                if success:
                    image = cv2.flip(image, 1)

                    image.flags.writeable = False

                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                    results = self._hands.process(image)
                    image.flags.writeable = True
                    if show_img:
                        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    if results.multi_hand_landmarks:
                        for hand_landmarks in results.multi_hand_landmarks:
                            landmark21 = []
                            for i in range(21):
                                x = hand_landmarks.landmark[i].x
                                y = hand_landmarks.landmark[i].y
                                z = hand_landmarks.landmark[i].z
                                landmark21.append((x, y, z))
                            landmark21_ = np.array([landmark21])
                            # Prediction by self-trained neural network
                            pre = self._my_model.predict(landmark21_[:1])
                            # Prediction probability > 0.5 is considered reliable
                            if np.max(pre) > 0.5:
                                ges_pre_p = np.argmax(pre)
                                self.now_ges = self._ges_dict[ges_pre_p]

                        # 显示我们预测的手势与概率
                        if show_img:
                            cv2.putText(image, str(np.max(pre)), (100, 200), 0, 1.3, (0, 0, 255), 3)
                            cv2.putText(image, self.now_ges, (0, 100), 0, 1.3, (0, 0, 255), 3)
                            # 将手部的特征点连线显示
                            for hand_landmarks in results.multi_hand_landmarks:
                                self._mp_drawing.draw_landmarks(
                                    image,
                                    hand_landmarks,
                                    self._mp_hands.HAND_CONNECTIONS,
                                    self._mp_drawing_styles.get_default_hand_landmarks_style(),
                                    self._mp_drawing_styles.get_default_hand_connections_style())
                    else:
                        self.now_ges = 'none'
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
        self._cap.release()
        cv2.destroyAllWindows()

    def start_in_thread(self):
        Thread(target=self.start_in_loop).start()  # ,name='recognizer')


recognizer = My_indentify()
# recognizer.start_in_thread()
