import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.ttk as tkk
import tkinter.font as font
haarcasecade_path = "C:\\Users\\yasht\\OneDrive\\Desktop\\Attendance-Management-system-using-face-recognition-master\\haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "C:\\Users\\yasht\\OneDrive\\Desktop\\Attendance-Management-system-using-face-recognition-master\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "C:\\Users\\yasht\\OneDrive\\Desktop\\Attendance-Management-system-using-face-recognition-master\\TrainingImage"
studentdetail_path = (
    "C:\\Users\\yasht\\OneDrive\\Desktop\\Attendance-Management-system-using-face-recognition-master\\StudentDetails\\studentdetails.csv"
)
attendance_path = "C:\\Users\\yasht\\OneDrive\\Desktop\\Attendance-Management-system-using-face-recognition-master\\Attendance"
def test_sys(l1,text_to_speech,):    
    #cam = cv2.VideoCapture(0)
    # ___, im = cam.read()
    im = cv2.imread(l1)
    df = pd.read_csv(studentdetail_path)
    facecasCade = cv2.CascadeClassifier(haarcasecade_path)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(trainimagelabel_path)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = facecasCade.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        global Id
        Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
        if conf < 70:
            print(conf)
            global Subject
            global aa
            global date
            global timeStamp
            aa = df.loc[df["Enrollment"] == Id]["Name"].values
            global tt
            tt = str(Id) + "-" + aa
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
            cv2.putText(
                im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4
            )
            res = "Face Recognized"
            text_to_speech(res)
        else:
            Id = "Unknown"
            tt = str(Id)
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
            cv2.putText(
                im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
            )
            res = "Face Not Recognized"
            text_to_speech(res)
    #cv2.destroyAllWindows()                    