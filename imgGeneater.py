import cv2
import os
def save_img(video_root):
    dirs=os.listdir(video_root)
    for dir in dirs:
        video_path=video_root+'/'+dir
        videos = os.listdir(video_path)
        for video_name in videos:
            file_name = video_name.split('.')[0]
            folder_name = video_path + file_name
            vc = cv2.VideoCapture(video_path+'/'+video_name)
            c=0
            rval=vc.isOpened()
            while rval:
                c = c + 1
                rval, frame = vc.read()
                pic_path = video_path+'/'
                if rval:
                    cv2.imwrite(pic_path +dir+str(c) + '.png', frame)
                    cv2.waitKey(1)
                else:
                    break
            vc.release()
            if os.path.exists(video_path+'/'+video_name):
                os.remove(video_path+'/'+video_name)
            else:
                print("The file does not exist")
            print('save_success')
            print(folder_name)


