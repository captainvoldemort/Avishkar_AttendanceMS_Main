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

#import fingerprint module
import fp

#implementing threading - libraries required
from threading import Thread

haarcasecade_path = "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/TrainingImageLabel/Trainner.yml"
)
trainimage_path = "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/TrainingImage"
studentdetail_path = (
    "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/StudentDetails/studentdetails.csv"
)
attendance_path = "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/Attendance"

# for choose subject and fill attendance
def subjectChoose(text_to_speech):
    def FillAttendance(tx):
        sub = tx
        now = time.time()
        future = now + 20  #time change 
        print(now)
        print(future)
        if sub == "":
            t = "Please enter the subject name!!!"
            print(t)
            #text_to_speech(t)
        else:
            #to fork system here for fingerprint recognition
            #thread = Thread(target=fp.save_attendance())
            #thread.start()
            print("Starting fingerprint attendance system...")
            fp.save_attendance()
            try:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                try:
                    recognizer.read(trainimagelabel_path)
                except:
                    e = "Model not found,please train model"
                    print(e)
                    #text_to_speech(e)
                facecasCade = cv2.CascadeClassifier(haarcasecade_path)
                df = pd.read_csv(studentdetail_path)
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ["Enrollment", "Name"]
                attendance = pd.DataFrame(columns=col_names)
                
                while True:
                    ___, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = facecasCade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
                        if conf < 70:
                            #print(conf)
                            global Subject
                            global aa
                            global date
                            global timeStamp
                            Subject = tx
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime(
                                "%Y-%m-%d"
                            )
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
                                "%H:%M:%S"
                            )
                            aa = df.loc[df["Enrollment"] == Id]["Name"].values
                            global tt
                            tt = str(Id) + "-" + aa
                            # En='1604501160'+str(Id)
                            attendance.loc[len(attendance)] = [
                                Id,
                                aa,
                            ]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4
                            )
                            #break_cam = 1
                        else:
                            Id = "Unknown"
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
                            )
                    if time.time() > future:
                        break
                    #if break_cam == 1:
                        #break

                    attendance = attendance.drop_duplicates(
                        ["Enrollment"], keep="first"
                    )
                    cv2.imshow("Filling Attendance...", im)
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:
                        break

                ts = time.time()
                print(aa)
                # attendance["date"] = date
                # attendance["Attendance"] = "P"
                attendance[date] = 1
                date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                Hour, Minute, Second = timeStamp.split(":")
                # fileName = "Attendance/" + Subject + ".csv"
                path = os.path.join(attendance_path, Subject)
                fileName = (
                    f"{path}/"
                    + Subject
                    + "_"
                    + date
                    + "_"
                    + Hour
                    + "-"
                    + Minute
                    + "-"
                    + Second
                    + ".csv"
                )
                #thread.join()
                attendance2 = fp.attendance1 
                #to perform inner join on fingerprint and face dataframe
                df_master = attendance.merge(attendance2,
                   on = 'Enrollment', 
                   how = 'inner')
                df_master = df_master.drop_duplicates(["Enrollment"], keep="first")
                #attendance = attendance.drop_duplicates(["Enrollment"], keep="first")
                #print("Trial 1 successful")
                print(df_master)
                df_master.to_csv(fileName,index=False)
                #print(attendance)
                #attendance.to_csv(fileName, index=False)
                #print("Trial 2 successful")
                m = "Attendance Filled Successfully of " + Subject
                print(m)
                #text_to_speech(m)
                #change temporary
                cam.release()
                cv2.destroyAllWindows()
                '''
                import csv
                import tkinter

                root = tkinter.Tk()
                root.title("Attendance of " + Subject)
                root.configure(background="white")
                cs = os.path.join(path, fileName)
                print(cs)
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:

                            label = tkinter.Label(
                                root,
                                width=10,
                                height=1,
                                fg="blue",
                                font=("times", 15, " bold "),
                                bg="white",
                                text=row,
                                relief=tkinter.RAISED,
                            )
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()
                print(attendance)
                '''
            except:
                f = "No Face found for attendance"
                print(f)
                #text_to_speech(f)
                cv2.destroyAllWindows()

    #check sheets function
    def Attf(tx):
        sub = tx
        if sub == "":
            t = "Please enter the subject name!!!"
            print(t)
            #text_to_speech(t)
        else:
            os.startfile(
                f"/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/Attendance/{sub}"
            )
    tx = input('Enter subject name: ')
    cho1 = input('Start attendance filling procedure? Enter y... ')
    if cho1 == 'y' or cho1 == 'Y':
        FillAttendance(tx)
    else:
        print('Invalid choice!!!')
        #exit()
