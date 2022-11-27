try:
   import tensorflow.python.keras as keras
except:
   import tensorflow.keras as keras
from keras.layers import Conv1D, BatchNormalization, Activation, Dropout, Flatten, Dense,AveragePooling1D
import numpy as np
from GlobalStates import resource_path
all_gestures=np.load(resource_path('DataForTraining/all_gestures.npy'),allow_pickle=True).tolist()


class MyModel(keras.Model):
  def __init__(self):
    super(MyModel, self).__init__()
    self.c1 = Conv1D(filters=1,kernel_size=2,padding='valid')
    self.b1=BatchNormalization()
    self.a1=Activation('relu')
    self.p1=AveragePooling1D(pool_size=2,strides=1,padding='valid')
    self.d1=Dropout(0.2)
    self.flatten = Flatten()
    self.f1=Dense(128,activation='relu')
    self.d2 = Dropout(0.2)
    self.f2=Dense(128,activation='relu')
    self.d3=Dropout(0.2)
    self.f3 = Dense(len(all_gestures), activation='softmax')

  def call(self, x):
    x = self.c1(x)
    x = self.b1(x)
    x = self.a1(x)
    x = self.p1(x)
    x = self.d1(x)
    x = self.flatten(x)
    x = self.d2(x)
    x=self.f2(x)
    x=self.d3(x)
    y = self.f3(x)
    return y


