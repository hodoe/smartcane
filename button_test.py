#!/usr/bin/env python

import RPi.GPIO as gpio
import time
import sys
import signal



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

signal.signal(signal.SIGINT, signal_handler)

gpio.setup(pin_btnA, gpio.IN)
gpio.setup(pin_btnB, gpio.IN)

prev_btnA = False
prev_btnB = False

btnNumber = 0

print ('BUTTON TEST')

try :
    while True :
        if gpio.input(pin_btnA) != prev_btnA:
            print('BUTTON A OCCUR !!!')
        if gpio.input(pin_btnB) != prev_btnB:
            print('BUTTON B OCCUR !!!')
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
