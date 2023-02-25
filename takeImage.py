import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time

#libraries for augmentation
'''
import imageio
import imgaug as ia
import imgaug.augmenters as iaa
'''

haarcasecade_path = "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/TrainingImageLabel/Trainner.yml"
)
trainimage_path = "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/TrainingImage"
studentdetail_path = (
    "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/StudentDetails/studentdetails.csv"
)
attendance_path = "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/Attendance"

# take Image of user
def TakeImage(l1, l2, haarcasecade_path, trainimage_path, text_to_speech):
    if (l1 == "") and (l2==""):
        t='Please Enter the your Enrollment Number and Name.'
        #text_to_speech(t)
        print(t)
    elif l1=='':
        t='Please Enter the your Enrollment Number.'
        #text_to_speech(t)
        print(t)
    elif l2 == "":
        t='Please Enter the your Name.'
        #text_to_speech(t)
        print(t)
    else:
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier(haarcasecade_path)
            Enrollment = l1
            Name = l2
            sampleNum = 0
            
            #change 1 - Due to error TypeError: unsupported operand type(s) for +: 'int' and 'str'
            Enrollment = str(Enrollment)
            directory = Enrollment + "_" + Name
            path = os.path.join(trainimage_path, directory)
            os.mkdir(path)
            while True:
                ret, img = cam.read()
                #makes captured rgb image to gray-scale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                #cv2.imshow(faces)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    sampleNum = sampleNum + 1
                    #save in grayscale
                    cv2.imwrite(
                        f"{path}/ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + str(sampleNum)
                        + ".jpg",
                        gray[y : y + h, x : x + w],
                    )
                    
                    '''

                    #Augmentation 1 Horizontal flip
                    hflip= iaa.Fliplr(p=1.0)
                    input_hf= hflip.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "hflip_"
                        +str(sampleNum)
                        + ".jpg",
                        input_hf,
                    )

                    #Augmentation 2 Vertical flip
                    vflip= iaa.Flipud(p=1.0) 
                    input_vf= vflip.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "vflip_"
                        +str(sampleNum)
                        + ".jpg",
                        input_vf,
                    )
                    
                    #Augmentation 3 Image rotation
                    rot1 = iaa.Affine(rotate=(-50,20))
                    input_rot1 = rot1.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "rot_"
                        +str(sampleNum)
                        + ".jpg",
                        input_rot1,
                    )

                    #Augmentation 4 crop image by 0.3*h
                    crop1 = iaa.Crop(percent=(0, 0.3)) 
                    input_crop1 = crop1.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "crp_"
                        +str(sampleNum)
                        + ".jpg",
                        input_crop1,
                    )

                    #Augmentation 5 add gaussian noise
                    noise=iaa.AdditiveGaussianNoise(10,40)
                    input_noise=noise.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "noi_"
                        +str(sampleNum)
                        + ".jpg",
                        input_noise,
                    )

                    #Augmentation 6 image shearing augmenter shears the image by random amounts ranging from -40 to 40 degrees
                    shear = iaa.Affine(shear=(-40,40))
                    input_shear=shear.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "shear_"
                        +str(sampleNum)
                        + ".jpg",
                        input_shear,
                    )

                    #Augmentation 7 Gamma contrast
                    contrast=iaa.GammaContrast((0.5, 2.0))
                    input_contrast = contrast.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "cont_"
                        +str(sampleNum)
                        + ".jpg",
                        input_contrast,
                    )

                    #Augmentation 8 sigmoid contrast
                    contrast_sig = iaa.SigmoidContrast(gain=(5, 10), cutoff=(0.4, 0.6))
                    sigmoid_contrast = contrast_sig.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "sigcont_"
                        +str(sampleNum)
                        + ".jpg",
                        sigmoid_contrast,
                    )

                    #Augmentation 9 linear contrast
                    contrast_lin = iaa.LinearContrast((0.6, 0.4))
                    linear_contrast = contrast_lin.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "lincont_"
                        +str(sampleNum)
                        + ".jpg",
                        linear_contrast,
                    )

                    #Augmentation 10 elastic transform
                    elastic = iaa.ElasticTransformation(alpha=60.0, sigma=4.0)
                    input_elastic = elastic.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "elt_"
                        +str(sampleNum)
                        + ".jpg",
                        input_elastic,
                    )

                    #Augmentation 11 Polar Warping
                    polar = iaa.WithPolarWarping(iaa.CropAndPad(percent=(-0.2, 0.7)))
                    input_polar = polar.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "pol_"
                        +str(sampleNum)
                        + ".jpg",
                        input_polar,
                    )

                    #Augmentation 12 jigsaw
                    jigsaw = iaa.Jigsaw(nb_rows=20, nb_cols=15, max_steps=(3, 7))
                    input_jigsaw = jigsaw.augment_image(gray[y : y + h, x : x + w])
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + "jig_"
                        +str(sampleNum)
                        + ".jpg",
                        input_jigsaw,
                    )
                    '''

                    cv2.imshow("Frame", img)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                elif sampleNum > 50:
                    break
            cam.release()
            cv2.destroyAllWindows()
            row = [Enrollment, Name]
            with open(
                "/home/rpiavishkar/Desktop/Avishkar_AttendanceMS_Main/StudentDetails/studentdetails.csv",
                "a+",
            ) as csvFile:
                writer = csv.writer(csvFile, delimiter=",")
                writer.writerow(row)
                csvFile.close()
            res = "Images Saved for ER No:" + Enrollment + " Name:" + Name
            print(res)
            #text_to_speech(res)
        except FileExistsError as F:
            F = "Student Data already exists"
            print(F)
            #text_to_speech(F)
