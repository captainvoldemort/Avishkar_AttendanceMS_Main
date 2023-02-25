import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *

def subjectchoose(text_to_speech):
    def calculate_attendance(tx):
        Subject = tx
        if Subject=="":
            t='Please enter the subject name.'
            print(t)
            #text_to_speech(t)
        os.chdir(
            f"/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/Attendance/{Subject}"
        )
        filenames = glob(
            f"/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/Attendance/{Subject}/{Subject}*.csv"
        )
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
            #newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv("attendance.csv", index=False)

        root = tkinter.Tk()
        root.title("Attendance of "+Subject)
        root.configure(background="white")
        cs = f"/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/Attendance/{Subject}/attendance.csv"
        with open(cs) as file:
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
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

    #check sheets function
    def Attf(tx):
        sub = tx
        if sub == "":
            t="Please enter the subject name!!!"
            #text_to_speech(t)
        else:
            os.startfile(
            f"/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/Attendance/{sub}"
            )

    tx = input('Enter Subject: ')
    print('a. Check records')
    print('b. Calculate attendance for subject')
    cho1 = input("Enter your choice: a/b...")
    if cho1 == 'a' or cho1 == 'A':
        Attf(tx)
    elif cho1 == 'b' or cho1 == 'B':
        calculate_attendance(tx)
    else:
        print("Invalid Choice!!!")
        #exit()
