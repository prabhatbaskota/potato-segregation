
import cv2 as cv
from cv2 import destroyAllWindows 
import numpy as np 
import serial

arduinoData = serial.Serial('com3', 9600)



def empty(a):
    pass

cv.namedWindow('Params')
cv.resizeWindow('Params',640,90)
cv.createTrackbar('Threshold1','Params',103,255,empty)
cv.createTrackbar('Threshold2','Params',39,255,empty)


#create function to generate contours
cap = cv.VideoCapture(1)
while True:
    bool, img = cap.read()
    #img = cv.imread('download.jpeg') 
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (7,7),1)
    thres1 = cv.getTrackbarPos('Threshold1','Params')
    thres2 = cv.getTrackbarPos('Threshold2','Params')
    imgCanny = cv.Canny(imgBlur,thres1,thres2)

    kernel = np.ones((5,5))
    imgDil = cv.dilate(imgCanny,kernel,iterations = 1)   
    contours,_ =cv.findContours(imgDil,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area >= 4000 and area <=10000:
            print('Small Potato')
            
            cv.drawContours(img,cnt,-1,(0,255,0),2)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv.boundingRect(approx) 
            #cv.rectangle(img,(x ,y ),(x+w ,y+h ),(255,0,0),4)

            text ='Area :' + str(int(area))
            cv.putText(img,text,
                    (x-35,y),cv.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),1)
            
            cmd = 'ONE'
            cmd = cmd+'\r'
            arduinoData.write(cmd.encode())
            


            cv.namedWindow('Results',cv.WINDOW_NORMAL)
            cv.resizeWindow('Results',800,800)
            cv.imshow('Results',img)

        elif area >= 45000 and area <=50000:
            print('Medium Potato')
            
            cv.drawContours(img,cnt,-1,(0,255,0),2)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv.boundingRect(approx) 
            #cv.rectangle(img,(x ,y ),(x+w ,y+h ),(255,0,0),4)

            text ='Area :' + str(int(area))
            cv.putText(img,text,
                    (x-35,y),cv.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),1)
            
            cmd = 'TWO'
            cmd = cmd+'\r'
            arduinoData.write(cmd.encode())
            


            cv.namedWindow('Results',cv.WINDOW_NORMAL)
            cv.resizeWindow('Results',800,800)
            cv.imshow('Results',img)
        elif area >=  and area <=5000:
            
            cv.drawContours(img,cnt,-1,(0,255,0),2)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv.boundingRect(approx) 
            #cv.rectangle(img,(x ,y ),(x+w ,y+h ),(255,0,0),4)

            text ='Area :' + str(int(area))
            cv.putText(img,text,
                    (x-35,y),cv.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),1)
            
            cmd = 'THREE'
            cmd = cmd+'\r'
            arduinoData.write(cmd.encode())
            print("Small Size")


        cv.namedWindow('Results',cv.WINDOW_NORMAL)
        cv.resizeWindow('Results',800,800)
        cv.imshow('Results',img)

        else:
            cv.namedWindow('Results',cv.WINDOW_NORMAL)
            cv.resizeWindow('Results',800,800)
            cv.imshow('Results',img)   

    if cv.waitKey(1) & 0xFF == ord('c'):
        destroyAllWindows
    

    

