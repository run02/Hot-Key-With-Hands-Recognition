from Model.myModel import MyModel
#有时候引用会出现问题,所以使用两种引用方式,如果第一种出错就用第二种
try:
   import tensorflow.python.keras as keras
except:
   import tensorflow.keras as keras
import numpy as np

def load_training_sets()->list:

    return

def training():
    #获取初步数据,打乱顺序送入模型训练
    x_train,y_train=load_training_sets()
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
    model.save('my_train_12_gestures2')
    #打印摘要
    model.summary()


