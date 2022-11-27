import os
from Model.myModel import MyModel

#有时候引用会出现问题,所以使用两种引用方式,如果第一种出错就用第二种
try:
   import tensorflow.python.keras as keras
except:
   import tensorflow.keras as keras
import numpy as np
from GlobalStates import resource_path

def load_training_sets()->list:
    all_gestures=np.load(resource_path('DataForTraining/all_gestures.npy'),allow_pickle=True).tolist()
    x_train=[]
    y_train=[]
    for id,gesture in enumerate(all_gestures):
        try:
            each_gesture_vedios_data=np.load(os.path.join(resource_path('DataForTraining'),gesture+'.npy'),allow_pickle=True).tolist()
            for each in each_gesture_vedios_data:
                for _21_3 in each:
                    x_train.append(_21_3)
                    y_train.append(id)
        except FileNotFoundError:
            pass

    x_train=np.array(x_train)
    y_train=np.array(y_train)
    print(x_train.shape)
    print(y_train.shape)
    return x_train,y_train

def training():
    #获取初步数据,打乱顺序送入模型训练
    x_train,y_train=load_training_sets()
    print(y_train)
    np.random.seed(111)
    np.random.shuffle(x_train)
    np.random.seed(111)
    np.random.shuffle(y_train)


    #加载模型
    model =MyModel()
    #配置优化器,损失函数,指标
    model.compile(optimizer='adam',
                  loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['sparse_categorical_accuracy'])

    #送入模型.开始训练
    model.fit(x_train, y_train, batch_size=128, epochs=50, validation_split=0.2, validation_freq=1)
    #保存模型
    model.save('TrainingOutput/ModelFiles')
    #打印摘要
    model.summary()
    landmark21_ = np.array([x_train[0]])
    # 输入神经网络进行预测，得到预测结果为每一种手势对应的概率
    pre =  model.predict(landmark21_[:1])
    print(pre)



