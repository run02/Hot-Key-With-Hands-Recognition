import cv2
import mediapipe as mp
import numpy as np
from file_resource_management import FileResources
from abstract_layer import GestureRecognitionCameraInterface


GESTURE_DICT = {
    0: 'cool',
    1: 'eight',
    2: 'fist',
    3: 'five',
    4: 'four',
    5: 'fuck',
    6: 'nine',
    7: 'one',
    8: 'seven',
    9: 'six',
    10: 'three',
    11: 'two'
}

def put_with_overwrite(queue, item):
    if queue.full():
        queue.get()
    queue.put(item)


class GestureRecognitionCamera(GestureRecognitionCameraInterface):
    def __init__(self):
        self.cap = None
        self.hands = None
        self.mp_hands = None
        self.mp_drawing_styles = None
        self.mp_drawing = None
        self.model = FileResources.ai_model
        self.gesture_dict = GESTURE_DICT
        self.NOT_RECOGNIZED = 'Not recognized'
        self.RELIABILITY = 0.5
        # self.show_image = False
        self.results = None
        self.mediapipe_hands_init()

    # def set_show_image(self, show_image: bool):
    #     self.show_image = show_image

    def recognize_gesture(self, frame) -> str:
        frame = cv2.flip(frame, 1)
        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                landmark21 = []
                for i in range(21):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    z = hand_landmarks.landmark[i].z
                    landmark21.append((x, y, z))
                landmark21_ = np.array([landmark21])
                pre = self.model.predict(landmark21_[:1])
                if np.max(pre) > self.RELIABILITY:
                    result = self.gesture_dict[np.argmax(pre)]
                else:
                    result = self.NOT_RECOGNIZED
        else:
            self.results = None
            result = self.NOT_RECOGNIZED
        return result
    # 这里有bug只能开一次,md先不管了
    def process_images(self, start_event, stop_event, output_queue, show_image):
        while start_event.is_set():
            if self.cap is None:
                self.cap = cv2.VideoCapture(0)

            success, frame = self.cap.read()
            if success:
                result = self.recognize_gesture(frame=frame)
                put_with_overwrite(output_queue, result)
                # 显示我们预测的手势与概率
                if show_image and self.results is not None:
                    cv2.putText(frame, result, (0, 100), 0, 1.3, (0, 0, 255), 3)
                    # 将手部的特征点连线显示
                    for hand_landmarks in self.results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            self.mp_hands.HAND_CONNECTIONS,
                            self.mp_drawing_styles.get_default_hand_landmarks_style(),
                            self.mp_drawing_styles.get_default_hand_connections_style()
                        )

                if show_image:
                    cv2.namedWindow('Gesture Recognition Client', cv2.WINDOW_NORMAL)
                    # 展示图片画面
                    cv2.imshow('Gesture Recognition Client', frame)
                    # 按esc键退出
                    if cv2.waitKey(5) & 0xFF == 27:
                        break

        if self.cap is not None:
            self.free()
            self.cap = None


    def free(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def mediapipe_hands_init(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(model_complexity=0, min_detection_confidence=0.8, min_tracking_confidence=0.8)


gestureRecognitionCamera = GestureRecognitionCamera()


# 只能是这样掉这种函数才能开进程, 用对象的会报错说不能序列化
def main(start_event, stop_event, output_queue, show_image):
    gestureRecognitionCamera.process_images(start_event, stop_event, output_queue,show_image)
