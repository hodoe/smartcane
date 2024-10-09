#!/usr/bin/env python

import RPi.GPIO as gpio
import time
import sys
import signal
from datetime import datetime
#import board
import os.path
import sys
import inspect
import os
import math
from subprocess import Popen
import subprocess
import cv2
from multiprocessing import Process, Value, Manager


gpio.setmode(gpio.BCM)
pin_trigger = 9
pin_echo = 11
pin_vib = 0
pin_led = 10
pin_lux = 17
pin_btnA = 27
pin_btnB = 22

def signal_handler(signal, frame): # ctrl + c -> exit program
        print('You pressed Ctrl+C!')
        sys.exit(0)

def speak(option, msg) :
    os.system("espeak {} '{}'".format(option,msg))
    

def cam_loop():
    global prev_camera_millis

    camCnt = 0

    capture = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while(True):
        ret, frame = capture.read()

        if flags['file_a'] == True:
            fname = '/home/pi/test/capture.jpg'
            cv2.imwrite(fname, frame)
            print('cv2.imwrite ', fname,'.jpg')
            
                    
            getVersion =  subprocess.Popen("/home/pi/MyDir/bin/Debug/TestTensorFlow_Lite", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            print("Read Data : ", version.decode())
            
            #  #4,6$
            getData = version.decode()
            getData= getData.replace("#","")
            getData= getData.replace("$","")
            getData= getData.replace("\n","")
            x = getData.split(",")
            print(x)
            
            speechData = ""
            
            if int(x[0]) != 0:
                speechData += x[0] + " car "
            if int(x[1]) != 0:
                speechData += x[1] + " person "
            
            if len(speechData) != 0:
                speechData += " detected."
            else :
                speechData = "No obejct detected."
            print(speechData)
            
            
            
            option = '-s 160 -p 95 -a 200 -v ko+f3'
            #msg = 'No Object Detected.'

            print('espeak', option, speechData)
            speak(option, speechData)
            
            flags['file_a'] = False
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()




def main_loop():
    signal.signal(signal.SIGINT, signal_handler)

    gpio.setup(pin_btnA, gpio.IN)
    gpio.setup(pin_btnB, gpio.IN)

    prev_btnA = False
    prev_btnB = False

    btnNumber = 0

    print ('SENSOR TEST')
    
    
    try :
        while True :
            if gpio.input(pin_btnA) != prev_btnA:
                print('BUTTON A OCCUR !!!')
                flags['file_a'] = True
            if gpio.input(pin_btnB) != prev_btnB:
                print('BUTTON B OCCUR !!!')
                flags['file_b'] = True
                f = open("/home/pi/test/btn.txt", 'w')
                btnNumber += 1
                f.write(str(btnNumber))
                f.close()
                print('btnNumber', btnNumber)
                
            prev_btnA = gpio.input(pin_btnA)
            prev_btnB = gpio.input(pin_btnB)

            
    except (KeyboardInterrupt, SystemExit):
        gpio.cleanup()
        sys.exit(0)
    except:
        gpio.cleanup()
    
    
    
    


if __name__ == "__main__":
    
    manager = Manager()
    flags = manager.dict({'file_a' : False, 'file_b' : False, 'file_c' : False, 'str_a' : ''})

    p1 = Process(target=cam_loop)
    p2 = Process(target=main_loop)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    
    
