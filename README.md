# 手势识别绑定快捷键



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