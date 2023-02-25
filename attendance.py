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
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance
import test_system
import fp


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()



haarcasecade_path = "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/TrainingImageLabel/Trainner.yml"
)
trainimage_path = "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/TrainingImage"
studentdetail_path = (
    "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/StudentDetails/studentdetails.csv"
)
attendance_path = "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/Attendance"

def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True

#window = Tk()

def get_num():
    """Use input() to get a valid number from 1 to 127. Retry till success!"""
    i = 0
    while (i > 127) or (i < 1):
        try:
            i = int(input("Enter ER.NO. from 1-127: "))
        except ValueError:
            pass
    return i

def newenroll():
    print('New Enrollment...')
    txt1 = input('Enter Name: ')
    txt2 = get_num()
    ready1 = input('''Press 'y' when ready to take face image (y): ''')
    if ready1 == 'y' or ready1=='Y':
        take_image(txt1,txt2)
    else:
        print('Invalid choice!!!')
        #exit()
    train1 = input('Train model? Enter y: ')
    if train1 == 'y' or train1 == 'Y':
        train_image()
    else:
        print('Invalid choice!!!')
        #exit()
    print('Starting fingerprint enrollment procedure...')
    ch1 = input("Enter y to begin fingerprint enrollment procedure: y... ")
    if ch1 == 'y' or 'Y':
        fp.sta = 1
        while fp.sta == 1:
            fp.enroll_finger(txt2)
    else:
        print("Invalid choice...")


def take_image(txt1,txt2):
    #l1 and l2 are name and er. no. 
    l2 = txt1
    l1 = txt2
    takeImage.TakeImage(
        l1,
        l2,
        haarcasecade_path,
        trainimage_path,
        text_to_speech,
    )

    
def train_image():
    trainImage.TrainImage(
        haarcasecade_path,
        trainimage_path,
        trainimagelabel_path,
        text_to_speech,
    )

#Mark Attendance
def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)

#View Attendance
def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

#window.mainloop()
while True:
    print('''MIT-WPU SCHOOL OF ECE''')
    print('''Welcome to Team Avishkar's Attendance Management system!''')
    print('''Face Recognition and Fingerprint based Attedance Management System''')
    print('''Select operation...''')
    print("a. New Enrollment")
    print("b. Mark Attendance")
    print("c. View Attendance")
    print("q. Quit")
    choice1 = input('Enter choice: ')
    if choice1 == 'a' or choice1 == 'A':
        newenroll()
    elif choice1 == 'b' or choice1 == 'B':
        automatic_attedance()
    elif choice1 == 'c' or choice1 == 'C':
        view_attendance()
    elif choice1 == 'q' or choice1 == 'Q':
        exit()
    else:
        print('Invalid choice!!!')
        #exit()