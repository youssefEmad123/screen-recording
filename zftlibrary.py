import cv2 as cv
from gtts import gTTS
import os
from pygame import mixer
def show(image):
    img=cv.imread(image)
    cv.imshow("image",img)
def video(video,title):
    video=cv.VideoCapture(video)
    while True:
        isTrue,frame=video.read()
        cv.imshow(title,frame)
        if cv.waitKey(1)==27:
            break
    video.release()
    cv.destroyAllWindows()
def speak(txt,lang):
    myfile=gTTS(text=txt,lang=lang)
    myfile.save("ZftLibrary.mp3")
    mixer.init()
    mixer.music.load("zftlibrary.mp3")
    mixer.music.play()
