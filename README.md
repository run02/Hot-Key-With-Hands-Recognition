# 手势识别绑定快捷键



## 基于

### 原理简介

使用mediapipe识别手部21个点,

使用tensorflow训练模型,根据21个点分出给定的手势

使用opencv-python提供的窗口展示画面.

识别出手势后使用keyboard按照设定自动按下指定的快捷键

使用PyQt5制作GUI,用户可通过桌面应用程序控制识别开启,关闭.

使用pyyaml读取保存的参数文件.

最后使用auto-py-to-exe操作pyinstaller打包文件







## 代码统计

![image-20221122183850946](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122183850946.png)





### 

## 简介

这是一款基于手势识别绑定快捷键的应用.

他可以识别出你的手势,然后根据识别的



```flow
st3=>start: start start
io5=>inputoutput: input: show_img
op8=>operation: ges_dict = np.load('./num_to_ss.npy', allow_pickle=True)
op10=>operation: ges_dict = ges_dict.tolist()
op12=>operation: my_model = keras.models.load_model('my_train_12_gestures2')
op14=>operation: mp_drawing = mp.solutions.drawing_utils
op16=>operation: mp_drawing_styles = mp.solutions.drawing_styles
op18=>operation: mp_hands = mp.solutions.hands
op20=>operation: hands = mp_hands.Hands(model_complexity=0, min_detection_confidence=0.8, min_tracking_confidence=0.8)
op22=>operation: now_ges = 'none'
op24=>operation: pre = []
cond27=>condition: while True
op194=>operation: image = get_image()
op196=>operation: image = cv2.flip(image, 1)
op198=>operation: image.flags.writeable = False
op200=>operation: image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
op202=>operation: results = hands.process(image)
op204=>operation: image.flags.writeable = True
op206=>operation: image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cond209=>condition: if results.multi_hand_landmarks
cond214=>condition: for hand_landmarks in results.multi_hand_landmarks
op261=>operation: landmark21 = []
cond264=>condition: for i in range(21)
op277=>operation: x = hand_landmarks.landmark[i].x
op279=>operation: y = hand_landmarks.landmark[i].y
op281=>operation: z = hand_landmarks.landmark[i].z
sub283=>subroutine: landmark21.append((x, y, z))
op287=>operation: landmark21_ = np.array([landmark21])
op289=>operation: pre = my_model.predict(landmark21_[:1])
cond292=>condition: if (np.max(pre) > 0.5)
op296=>operation: ges_pre_p = np.argmax(pre)
op298=>operation: now_ges = ges_dict[ges_pre_p]
cond306=>condition: if show_img
sub310=>subroutine: cv2.putText(image, str(np.max(pre)), (100, 200), 0, 1.3, (0, 0, 255), 3)
sub312=>subroutine: cv2.putText(image, now_ges, (0, 100), 0, 1.3, (0, 0, 255), 3)
cond315=>operation: mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style()) while  hand_landmarks in results.multi_hand_landmarks
cond334=>condition: if show_img
sub338=>subroutine: cv2.namedWindow('Gesture Recognition Client', cv2.WINDOW_NORMAL)
sub340=>subroutine: cv2.imshow('Gesture Recognition Client', image)
cond343=>operation: break if  ((cv2.waitKey(5) & 255) == 27)
e358=>end: end start

st3->io5
io5->op8
op8->op10
op10->op12
op12->op14
op14->op16
op16->op18
op18->op20
op20->op22
op22->op24
op24->cond27
cond27(yes)->op194
op194->op196
op196->op198
op198->op200
op200->op202
op202->op204
op204->op206
op206->cond209
cond209(yes)->cond214
cond214(yes)->op261
op261->cond264
cond264(yes)->op277
op277->op279
op279->op281
op281->sub283
sub283(left)->cond264
cond264(no)->op287
op287->op289
op289->cond292
cond292(yes)->op296
op296->op298
op298->cond214
cond292(no)->cond214
cond214(no)->cond306
cond306(yes)->sub310
sub310->sub312
sub312->cond315
cond315->cond334
cond334(yes)->sub338
sub338->sub340
sub340->cond343
cond343->cond27
cond334(no)->cond27
cond306(no)->cond334
cond209(no)->cond334
cond27(no)->e358




```

## 打包

![image-20221122162018882](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122162018882.png)





![image-20221122162106756](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122162106756.png)



```flow
st3=>start: start start_in_loop
io5=>inputoutput: input: self, show_img
op8=>operation: self.cap = cv2.VideoCapture(0)
cond11=>condition: while True
cond199=>condition: if (MyGlobalStates.__run__ is True)
op203=>operation: (success, image) = self.cap.read()
cond206=>condition: if success
op210=>operation: image = cv2.flip(image, 1)
op212=>operation: image.flags.writeable = False
op214=>operation: image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
op216=>operation: results = self.hands.process(image)
op218=>operation: image.flags.writeable = True
op220=>operation: image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cond223=>condition: if results.multi_hand_landmarks
cond228=>condition: for hand_landmarks in results.multi_hand_landmarks
op275=>operation: landmark21 = []
cond278=>condition: for i in range(21)
op291=>operation: x = hand_landmarks.landmark[i].x
op293=>operation: y = hand_landmarks.landmark[i].y
op295=>operation: z = hand_landmarks.landmark[i].z
sub297=>subroutine: landmark21.append((x, y, z))
op301=>operation: landmark21_ = np.array([landmark21])
op303=>operation: pre = self.my_model.predict(landmark21_[:1])
cond306=>condition: if (np.max(pre) > 0.5)
op310=>operation: ges_pre_p = np.argmax(pre)
op312=>operation: self.now_ges = self.ges_dict[ges_pre_p]
cond320=>condition: if show_img
sub324=>subroutine: cv2.putText(image, str(np.max(pre)), (100, 200), 0, 1.3, (0, 0, 255), 3)
sub326=>subroutine: cv2.putText(image, self.now_ges, (0, 100), 0, 1.3, (0, 0, 255), 3)
cond329=>operation: self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS, self.mp_drawing_styles.get_default_hand_landmarks_style(), self.mp_drawing_styles.get_default_hand_connections_style()) while  hand_landmarks in results.multi_hand_landmarks
cond350=>condition: if show_img
sub354=>subroutine: cv2.namedWindow('Gesture Recognition Client', cv2.WINDOW_NORMAL)
sub356=>subroutine: cv2.imshow('Gesture Recognition Client', image)
cond359=>operation: break if  ((cv2.waitKey(5) & 255) == 27)
op346=>operation: self.now_ges = 'none'
sub377=>subroutine: break
sub382=>subroutine: self.free()
e384=>end: end start_in_loop

st3->io5
io5->op8
op8->cond11
cond11(yes)->cond199
cond199(yes)->op203
op203->cond206
cond206(yes)->op210
op210->op212
op212->op214
op214->op216
op216->op218
op218->op220
op220->cond223
cond223(yes)->cond228
cond228(yes)->op275
op275->cond278
cond278(yes)->op291
op291->op293
op293->op295
op295->sub297
sub297(left)->cond278
cond278(no)->op301
op301->op303
op303->cond306
cond306(yes)->op310
op310->op312
op312->cond228
cond306(no)->cond228
cond228(no)->cond320
cond320(yes)->sub324
sub324->sub326
sub326->cond329
cond329->cond350
cond350(yes)->sub354
sub354->sub356
sub356->cond359
cond359->cond11
cond350(no)->cond11
cond320(no)->cond350
cond223(no)->op346
op346->cond350
cond206(no)->cond11
cond199(no)->sub377
cond11(no)->sub382
sub382->e384


```

## 简介



### 目前最多可以识别出这些手势:

<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122185705967.png" alt="image-20221122185705967" style="zoom: 50%;" />

​     

<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122185736690.png" alt="image-20221122185736690" style="zoom:50%;" />



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122185754782.png" alt="image-20221122185754782" style="zoom:50%;" />



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122185837820.png" alt="image-20221122185837820" style="zoom:50%;" />



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122185858200.png" alt="image-20221122185858200" style="zoom:50%;" />



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122185916507.png" alt="image-20221122185916507" style="zoom:50%;" />



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122185934707.png" alt="image-20221122185934707" style="zoom:50%;" />





<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122185952538.png" alt="image-20221122185952538" style="zoom:50%;" />





<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122190004002.png" alt="image-20221122190004002" style="zoom:50%;" />



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122190026476.png" alt="image-20221122190026476" style="zoom:50%;" />



<img src="https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122190039590.png" alt="image-20221122190039590" style="zoom:50%;" />

## 函数介绍

#### 类

其中now_ges是共享给外部的变量,其它的是函数内部使用的变量

start_in_loop会在死循环中调用识别算法,直到全局控制位为False后退出.

start_in_thread是共享给外部的调用方法,每次调用会新开启一个线程运行start_in_loop方法.

![image-20221122195924251](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221122195924251.png)



#### 初始化函数

```python
def __init__(self):
```

```py
 def __init__(self):
        # self.ges_dict = np.load('assets/num_to_ss.npy', allow_pickle=True) #识别出来的手势是数字,需要用字典把序号转化成字符串,加载保存的对照表
        # self.ges_dict = self.ges_dict.tolist()
        self._ges_dict = {0: 'cool', 1: 'eight', 2: 'fist', 3: 'five',
                          4: 'four', 5: 'fuck', 6: 'nine', 7: 'one', 8: 'seven',
                          9: 'six', 10: 'three', 11: 'two'}

        print(self._ges_dict)
        self._my_model = load_model(resource_path('assets/my_train_12_gestures2')) # 加载训练好的tensorflow模型
        self._mp_drawing = mp.solutions.drawing_utils  # 创建一个绘图工具
        self._mp_drawing_styles = mp.solutions.drawing_styles  # 创建一个绘图样式
        self._mp_hands = mp.solutions.hands  # 创建mediapipe框架读取特征点的初步工具，需要输入一个视频流，后通过自定义的tenslrflow神经网络获得手势预测值
        self._hands = self._mp_hands.Hands(model_complexity=0, min_detection_confidence=0.8, min_tracking_confidence=0.8)
        self.now_ges = 'none' #用于共享出去,给其他程序获得手势的标志位
        self._pre = []  # tensorflow模型预测输出为一个包含12个权值的list
```

```flow
st3=>start: start __init__
io5=>inputoutput: input: self
op8=>operation: self._ges_dict = {0: 'cool', 1: 'eight', 2: 'fist', 3: 'five', 4: 'four', 5: 'fuck', 6: 'nine', 7: 'one', 8: 'seven', 9: 'six', 10: 'three', 11: 'two'}
sub10=>subroutine: print(self._ges_dict)
op12=>operation: self._my_model = load_model(resource_path('assets/my_train_12_gestures2'))
op14=>operation: self._mp_drawing = mp.solutions.drawing_utils
op16=>operation: self._mp_drawing_styles = mp.solutions.drawing_styles
op18=>operation: self._mp_hands = mp.solutions.hands
op20=>operation: self._hands = self._mp_hands.Hands(model_complexity=0, min_detection_confidence=0.8, min_tracking_confidence=0.8)
op22=>operation: self.now_ges = 'none'
op24=>operation: self._pre = []
e26=>end: end __init__

st3->io5
io5->op8
op8->sub10
sub10->op12
op12->op14
op14->op16
op16->op18
op18->op20
op20->op22
op22->op24
op24->e26


```



#### 开启大循环函数

```py
def start_in_loop(self,show_img=True):
```



```py
def start_in_loop(self,show_img=True):
    self._cap=cv2.VideoCapture(0)
    while True:
        if MyGlobalStates.__run__ is True:
            # time.sleep(0.05)
            # 从摄像头读一帧画面
            success, image = self._cap.read()
            if success:
                image = cv2.flip(image, 1)
                # 将图片设置为不可写，提升性能
                image.flags.writeable = False
                # 转换为RGB格式
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                # 调用mediapipe框架读取特征点，特征点为1个对象，保存在results中
                results = self._hands.process(image)
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
                        pre = self._my_model.predict(landmark21_[:1])
                        # 预测结果大于0.5认为结果可信，进入下一步判断，可更改该值获得更高或较低的可信度
                        if np.max(pre) > 0.5:
                            # 得到预测结概率最大的手势的编号
                            ges_pre_p = np.argmax(pre)
                            # 将手势编号通过字典转化为我们给他起名的字符串
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
```

```flow
st3=>start: start start_in_loop
io5=>inputoutput: input: self, show_img
op8=>operation: self._cap = cv2.VideoCapture(0)
cond11=>condition: while True
cond199=>condition: if (MyGlobalStates.__run__ is True)
op203=>operation: (success, image) = self._cap.read()
cond206=>condition: if success
op210=>operation: image = cv2.flip(image, 1)
op212=>operation: image.flags.writeable = False
op214=>operation: image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
op216=>operation: results = self._hands.process(image)
op218=>operation: image.flags.writeable = True
op220=>operation: image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cond223=>condition: if results.multi_hand_landmarks
cond228=>condition: for hand_landmarks in results.multi_hand_landmarks
op275=>operation: landmark21 = []
cond278=>condition: for i in range(21)
op291=>operation: x = hand_landmarks.landmark[i].x
op293=>operation: y = hand_landmarks.landmark[i].y
op295=>operation: z = hand_landmarks.landmark[i].z
sub297=>subroutine: landmark21.append((x, y, z))
op301=>operation: landmark21_ = np.array([landmark21])
op303=>operation: pre = self._my_model.predict(landmark21_[:1])
cond306=>condition: if (np.max(pre) > 0.5)
op310=>operation: ges_pre_p = np.argmax(pre)
op312=>operation: self.now_ges = self._ges_dict[ges_pre_p]
cond320=>condition: if show_img
sub324=>subroutine: cv2.putText(image, str(np.max(pre)), (100, 200), 0, 1.3, (0, 0, 255), 3)
sub326=>subroutine: cv2.putText(image, self.now_ges, (0, 100), 0, 1.3, (0, 0, 255), 3)
cond329=>operation: self._mp_drawing.draw_landmarks(image, hand_landmarks, self._mp_hands.HAND_CONNECTIONS, self._mp_drawing_styles.get_default_hand_landmarks_style(), self._mp_drawing_styles.get_default_hand_connections_style()) while  hand_landmarks in results.multi_hand_landmarks
cond350=>condition: if show_img
sub354=>subroutine: cv2.namedWindow('Gesture Recognition Client', cv2.WINDOW_NORMAL)
sub356=>subroutine: cv2.imshow('Gesture Recognition Client', image)
cond359=>operation: break if  ((cv2.waitKey(5) & 255) == 27)
op346=>operation: self.now_ges = 'none'
sub377=>subroutine: break
sub382=>subroutine: self.free()
e384=>end: end start_in_loop

st3->io5
io5->op8
op8->cond11
cond11(yes)->cond199
cond199(yes)->op203
op203->cond206
cond206(yes)->op210
op210->op212
op212->op214
op214->op216
op216->op218
op218->op220
op220->cond223
cond223(yes)->cond228
cond228(yes)->op275
op275->cond278
cond278(yes)->op291
op291->op293
op293->op295
op295->sub297
sub297(left)->cond278
cond278(no)->op301
op301->op303
op303->cond306
cond306(yes)->op310
op310->op312
op312->cond228
cond306(no)->cond228
cond228(no)->cond320
cond320(yes)->sub324
sub324->sub326
sub326->cond329
cond329->cond350
cond350(yes)->sub354
sub354->sub356
sub356->cond359
cond359->cond11
cond350(no)->cond11
cond320(no)->cond350
cond223(no)->op346
op346->cond350
cond206(no)->cond11
cond199(no)->sub377
cond11(no)->sub382
sub382->e384


```



#### 在线程中开启

```python
def start_in_thread(self):
    Thread(target=self.start_in_loop).start()#,name='recognizer')
```

#### 释放内存

```python
def free(self):
    self._cap.release()
    cv2.destroyAllWindows()
```

```flow
st3=>start: start free
io5=>inputoutput: input: self
sub8=>subroutine: self._cap.release()
sub10=>subroutine: cv2.destroyAllWindows()
e12=>end: end free

st3->io5
io5->sub8
sub8->sub10
sub10->e12


```



#### 加载快捷键

```python
def load(file=resource_path("assets/bind.yml"))->dict:
    with open(file, 'r', encoding='utf-8') as f:
        binds = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    return binds

```



#### 等待按键信号并按下快捷键

```py
def waiting_to_press_and_release():
    global binds
    while True:
        if MyGlobalStates.__run__:
            if recognizer.now_ges in binds.keys():
                if binds[recognizer.now_ges]!='nothing':
                    keyboard.press_and_release(binds[recognizer.now_ges])
            time.sleep(0.2)
        else:
            break
```



#### 重新加载

```python
def reloads():
    global binds
    binds=load()
```



#### 在线程中开启

```py
#等待开启的线程
def start_in_thread():
    Thread(target=waiting_to_press_and_release).start()
```

```python
st3=>start: start start_in_thread
io5=>inputoutput: input: self
sub8=>subroutine: Thread(target=self.start_in_loop).start()
e10=>end: end start_in_thread

st3->io5
io5->sub8
sub8->e10


```



#### 加载UI

```py
def set_UI(self):
        self.setWindowTitle("Hot-Key-With-Hands-Recognition-V0.1")
        # self.resize(400, 100)
        hlayout = QHBoxLayout()
        fromlayout = QFormLayout()

        self.state_label = QLabel('Status')
        self.state = QLabel(' OFF')
        self.btn_start = QPushButton('Start')
        self.btn_end = QPushButton('Close')

        hlayout.addWidget(self.state_label)
        hlayout.addWidget(self.state)
        hlayout.addWidget(self.btn_start)
        hlayout.addWidget(self.btn_end)

        fromlayout.addRow(hlayout)
        self.click_btns=[]
        self.edits=[]
        self.labels=[]

        l1=QLabel('one')
        l2=QLabel('two')
        l3=QLabel('three')
        l4=QLabel('four')
        l5=QLabel('five')
        l6=QLabel('six')
        l7=QLabel('seven')
        l8=QLabel('eight')
        l9=QLabel('nine')
        lfi=QLabel('fist')
        lfu=QLabel('fuck')
        lc=QLabel('cool')

        self.labels.append(l1)
        self.labels.append(l2)
        self.labels.append(l3)
        self.labels.append(l4)
        self.labels.append(l5)
        self.labels.append(l6)
        self.labels.append(l7)
        self.labels.append(l8)
        self.labels.append(l9)
        self.labels.append(lfi)
        self.labels.append(lfu)
        self.labels.append(lc)

        _one=  MyLineEdit(binds['one'])
        _two = MyLineEdit(binds['two'])
        _three = MyLineEdit(binds['three'])
        _four = MyLineEdit(binds['four'])
        _five = MyLineEdit(binds['five'])
        _six = MyLineEdit(binds['six'])
        _seven= MyLineEdit(binds['seven'])
        _eight = MyLineEdit(binds['eight'])
        _nine= MyLineEdit(binds['nine'])
        _fist = MyLineEdit(binds['fist'])
        _fuck = MyLineEdit(binds['fuck'])
        _cool = MyLineEdit(binds['cool'])

        self.edits.append(_one)
        self.edits.append(_two)
        self.edits.append(_three)
        self.edits.append(_four)
        self.edits.append(_five)
        self.edits.append(_six)
        self.edits.append(_seven)
        self.edits.append(_eight)
        self.edits.append(_nine)
        self.edits.append(_fist)
        self.edits.append(_fuck)
        self.edits.append(_cool)

        # for e in self.edits:
        #     e.setFocusProxy(Qt.NoFocus)

        for i in range(len(binds.keys())):
            vlayout = QHBoxLayout()

            btn=QPushButton('Save')

            self.click_btns.append(btn)
            # PATH = QLineEdit(self.edits[i])
            # PATH.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑

            vlayout.addWidget(self.labels[i])
            vlayout.addWidget(self.edits[i])
            fromlayout.addRow(btn,vlayout)

        self.setLayout(fromlayout)
        MyGlobalStates.__run__ = False

    
```

```flow
st3=>start: start set_UI
io5=>inputoutput: input: self
sub8=>subroutine: self.setWindowTitle('Hot-Key-With-Hands-Recognition-V0.1')
op10=>operation: hlayout = QHBoxLayout()
op12=>operation: fromlayout = QFormLayout()
op14=>operation: self.state_label = QLabel('Status')
op16=>operation: self.state = QLabel(' OFF')
op18=>operation: self.btn_start = QPushButton('Start')
op20=>operation: self.btn_end = QPushButton('Close')
sub22=>subroutine: hlayout.addWidget(self.state_label)
sub24=>subroutine: hlayout.addWidget(self.state)
sub26=>subroutine: hlayout.addWidget(self.btn_start)
sub28=>subroutine: hlayout.addWidget(self.btn_end)
sub30=>subroutine: fromlayout.addRow(hlayout)
op32=>operation: self.click_btns = []
op34=>operation: self.edits = []
op36=>operation: self.labels = []
op38=>operation: l1 = QLabel('one')
op40=>operation: l2 = QLabel('two')
op42=>operation: l3 = QLabel('three')
op44=>operation: l4 = QLabel('four')
op46=>operation: l5 = QLabel('five')
op48=>operation: l6 = QLabel('six')
op50=>operation: l7 = QLabel('seven')
op52=>operation: l8 = QLabel('eight')
op54=>operation: l9 = QLabel('nine')
op56=>operation: lfi = QLabel('fist')
op58=>operation: lfu = QLabel('fuck')
op60=>operation: lc = QLabel('cool')
sub62=>subroutine: self.labels.append(l1)
sub64=>subroutine: self.labels.append(l2)
sub66=>subroutine: self.labels.append(l3)
sub68=>subroutine: self.labels.append(l4)
sub70=>subroutine: self.labels.append(l5)
sub72=>subroutine: self.labels.append(l6)
sub74=>subroutine: self.labels.append(l7)
sub76=>subroutine: self.labels.append(l8)
sub78=>subroutine: self.labels.append(l9)
sub80=>subroutine: self.labels.append(lfi)
sub82=>subroutine: self.labels.append(lfu)
sub84=>subroutine: self.labels.append(lc)
op86=>operation: _one = MyLineEdit(binds['one'])
op88=>operation: _two = MyLineEdit(binds['two'])
op90=>operation: _three = MyLineEdit(binds['three'])
op92=>operation: _four = MyLineEdit(binds['four'])
op94=>operation: _five = MyLineEdit(binds['five'])
op96=>operation: _six = MyLineEdit(binds['six'])
op98=>operation: _seven = MyLineEdit(binds['seven'])
op100=>operation: _eight = MyLineEdit(binds['eight'])
op102=>operation: _nine = MyLineEdit(binds['nine'])
op104=>operation: _fist = MyLineEdit(binds['fist'])
op106=>operation: _fuck = MyLineEdit(binds['fuck'])
op108=>operation: _cool = MyLineEdit(binds['cool'])
sub110=>subroutine: self.edits.append(_one)
sub112=>subroutine: self.edits.append(_two)
sub114=>subroutine: self.edits.append(_three)
sub116=>subroutine: self.edits.append(_four)
sub118=>subroutine: self.edits.append(_five)
sub120=>subroutine: self.edits.append(_six)
sub122=>subroutine: self.edits.append(_seven)
sub124=>subroutine: self.edits.append(_eight)
sub126=>subroutine: self.edits.append(_nine)
sub128=>subroutine: self.edits.append(_fist)
sub130=>subroutine: self.edits.append(_fuck)
sub132=>subroutine: self.edits.append(_cool)
cond135=>condition: for i in range(len(binds.keys()))
op152=>operation: vlayout = QHBoxLayout()
op154=>operation: btn = QPushButton('Save')
sub156=>subroutine: self.click_btns.append(btn)
sub158=>subroutine: vlayout.addWidget(self.labels[i])
sub160=>subroutine: vlayout.addWidget(self.edits[i])
sub162=>subroutine: fromlayout.addRow(btn, vlayout)
sub166=>subroutine: self.setLayout(fromlayout)
op168=>operation: MyGlobalStates.__run__ = False
e170=>end: end set_UI

st3->io5
io5->sub8
sub8->op10
op10->op12
op12->op14
op14->op16
op16->op18
op18->op20
op20->sub22
sub22->sub24
sub24->sub26
sub26->sub28
sub28->sub30
sub30->op32
op32->op34
op34->op36
op36->op38
op38->op40
op40->op42
op42->op44
op44->op46
op46->op48
op48->op50
op50->op52
op52->op54
op54->op56
op56->op58
op58->op60
op60->sub62
sub62->sub64
sub64->sub66
sub66->sub68
sub68->sub70
sub70->sub72
sub72->sub74
sub74->sub76
sub76->sub78
sub78->sub80
sub80->sub82
sub82->sub84
sub84->op86
op86->op88
op88->op90
op90->op92
op92->op94
op94->op96
op96->op98
op98->op100
op100->op102
op102->op104
op104->op106
op106->op108
op108->sub110
sub110->sub112
sub112->sub114
sub114->sub116
sub116->sub118
sub118->sub120
sub120->sub122
sub122->sub124
sub124->sub126
sub126->sub128
sub128->sub130
sub130->sub132
sub132->cond135
cond135(yes)->op152
op152->op154
op154->sub156
sub156->sub158
sub158->sub160
sub160->sub162
sub162(left)->cond135
cond135(no)->sub166
sub166->op168
op168->e170


```



#### 设置回调函数

```python
def set_callbacks(self):
        #绑定开始和结束按钮的按键,按下后修改全局状态标志位,修改开关状态的标签
        self.btn_start.clicked.connect(self.btn_start_callback)#这里差了一个回调函数
        self.btn_end.clicked.connect(self.btn_end_callback)
        self.edits[0].textChanged.connect(lambda: self.show_edits_change(0))
        self.edits[1].textChanged.connect(lambda: self.show_edits_change(1))
        self.edits[2].textChanged.connect(lambda: self.show_edits_change(2))
        self.edits[3].textChanged.connect(lambda: self.show_edits_change(3))
        self.edits[4].textChanged.connect(lambda: self.show_edits_change(4))
        self.edits[5].textChanged.connect(lambda: self.show_edits_change(5))
        self.edits[6].textChanged.connect(lambda: self.show_edits_change(6))
        self.edits[7].textChanged.connect(lambda: self.show_edits_change(7))
        self.edits[8].textChanged.connect(lambda: self.show_edits_change(8))
        self.edits[9].textChanged.connect(lambda: self.show_edits_change(9))
        self.edits[10].textChanged.connect(lambda: self.show_edits_change(10))
        self.edits[11].textChanged.connect(lambda: self.show_edits_change(11))

        for btn in self.click_btns:
            btn.clicked.connect(self.save_binds_and_reload)


```



```flow
st3=>start: start set_callbacks
io5=>inputoutput: input: self
sub8=>subroutine: self.btn_start.clicked.connect(self.btn_start_callback)
sub10=>subroutine: self.btn_end.clicked.connect(self.btn_end_callback)
sub12=>subroutine: self.edits[0].textChanged.connect((lambda : self.show_edits_change(0)))
sub14=>subroutine: self.edits[1].textChanged.connect((lambda : self.show_edits_change(1)))
sub16=>subroutine: self.edits[2].textChanged.connect((lambda : self.show_edits_change(2)))
sub18=>subroutine: self.edits[3].textChanged.connect((lambda : self.show_edits_change(3)))
sub20=>subroutine: self.edits[4].textChanged.connect((lambda : self.show_edits_change(4)))
sub22=>subroutine: self.edits[5].textChanged.connect((lambda : self.show_edits_change(5)))
sub24=>subroutine: self.edits[6].textChanged.connect((lambda : self.show_edits_change(6)))
sub26=>subroutine: self.edits[7].textChanged.connect((lambda : self.show_edits_change(7)))
sub28=>subroutine: self.edits[8].textChanged.connect((lambda : self.show_edits_change(8)))
sub30=>subroutine: self.edits[9].textChanged.connect((lambda : self.show_edits_change(9)))
sub32=>subroutine: self.edits[10].textChanged.connect((lambda : self.show_edits_change(10)))
sub34=>subroutine: self.edits[11].textChanged.connect((lambda : self.show_edits_change(11)))
cond37=>operation: btn.clicked.connect(self.save_binds_and_reload) while  btn in self.click_btns
e49=>end: end set_callbacks

st3->io5
io5->sub8
sub8->sub10
sub10->sub12
sub12->sub14
sub14->sub16
sub16->sub18
sub18->sub20
sub20->sub22
sub22->sub24
sub24->sub26
sub26->sub28
sub28->sub30
sub30->sub32
sub32->sub34
sub34->cond37
cond37->e49


```



#### 每个回调函数

```python
def btn_start_callback(self):
        if MyGlobalStates.__run__ == False:
            try:
                self.state.setText('On')
                MyGlobalStates.__run__=True
                recognizer.start_in_thread()
                start_in_thread()
            except Exception as e:
                QMessageBox.information(self, 'Error', e, QMessageBox.Ok)

    
```



```py
def btn_end_callback(self):
        self.state.setText('Close')
        MyGlobalStates.__run__=False

  
```



```py
def show_edits_change(self,idx):
        binds[list(binds.keys())[idx]]=self.edits[idx].text()

   
```





```python
def save_binds_and_reload(self):
        with open(resource_path('assets/bind.yml'),'w',encoding='utf-8') as f:
            f.write("#ALL_Gesture: {0: 'cool', 1: 'eight', 2: 'fist', 3: 'five', 4: 'four', 5: 'fuck', 6: 'nine', 7: 'one', 8: 'seven', 9: 'six', 10: 'three', 11: 'two'}\n")
            #保存配置
            for k in binds.keys():
                f.write(f"{k}: {binds[k]}\n")
            f.close()
        reloads()
        QMessageBox.information(self, 'Saving Changes', 'Saved Successfully !', QMessageBox.Ok)

 
```



```python
def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        MyGlobalStates.__run__=False


```



```python
def start_gui():
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
```

