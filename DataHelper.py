#%%
import cv2
import os
import mediapipe as mp
import numpy as np
class Helper:
    def __init__(self,path:str):
        self.img_root_path =path
        self.mp_hands = mp.solutions.hands
        self.dictionary = self.generate_dictionary(self.get_gestures(self.img_root_path))
        np.save('ss_to_num',self.dictionary)
        self.dictionary_ges = {v: k for k, v in self.dictionary.items()}
        np.save('num_to_ss',self.dictionary_ges)
        self.gestures = self.get_gestures(self.img_root_path)
        self.x_tr = []
        self.x_train = []
        self.y_train = []

    def read_path(self,file_pathname):    #遍历该目录下的所有图片文件
        imglist = []

        for filename in os.listdir(file_pathname):
            #print(filename)
            filename=file_pathname+'/'+filename
            imglist.append(str(filename))
        return imglist

    def get_gestures(self,folder):
        g=[]
        for gesture in os.listdir(folder):
            g.append(gesture)
        return g

    def generate_dictionary(self,g):
        d={}
        for idx,ges in enumerate(g):
            d.update({ges:idx})
        return d



    def get_train_data(self):
        with self.mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=1,
            min_detection_confidence=0.9) as hands:
         for gesture in self.gestures:
            x=self.img_root_path+'/'+gesture
            IMAGE_FILES = self.read_path(x)
            for idx, file in enumerate(IMAGE_FILES):
            # Read an image, flip it around y-axis for correct handedness output (see
            # above).
                image = cv2.flip(cv2.imread(file), 1)
                # Convert the BGR image to RGB before processing.
                results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                if not results.multi_hand_landmarks:
                  continue
                image_height, image_width, _ = image.shape
                annotated_image = image.copy()
                for hand_landmarks in results.multi_hand_landmarks:#到这里是一堆手的图片的结果
                    x_tr = []
                    for i in range(21):#从第一个开始提取每一个手的坐标，转成数组
                        x_tr.append((hand_landmarks.landmark[i].x, hand_landmarks.landmark[i].y, hand_landmarks.landmark[i].z))

                    self.x_train.append(x_tr)
                    self.y_train.append((self.dictionary[gesture]))

        self.x_train=np.array(self.x_train)
        self.y_train=np.array(self.y_train)
        np.save('x_train.npy',self.x_train)
        np.save('y_train.npy', self.y_train)
        print(f'x_train.shape : ',self.x_train.shape, 'y_train.shape : ',self.y_train.shape)
        return self.x_train,self.y_train
if __name__ == '__main__':
    pass
    # a=Helper('./ss')
    # b=a.get_train_data()
