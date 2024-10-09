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

gpio.setup(pin_trigger, gpio.OUT)
gpio.setup(pin_echo, gpio.IN)
gpio.setup(pin_vib, gpio.OUT)

time.sleep(0.5)

print ('ULTRA - VIB TEST')

try :
    while True :
        gpio.output(pin_trigger, False)
        time.sleep(0.1)
        gpio.output(pin_trigger, True)
        time.sleep(0.00001)
        gpio.output(pin_trigger, False)

        myStartingTime = time.time()
        while gpio.input(pin_echo) == 0 :
            pulse_start = time.time()
            if pulse_start - myStartingTime > 1:
                break
        myStartingTime = time.time()
        while gpio.input(pin_echo) == 1 :
            pulse_end = time.time()
            if pulse_end - myStartingTime > 1:
                break
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        if pulse_duration >=0.01746:
            # print('time out')
            continue
        elif distance > 300 or distance==0:
            # print('out of range')
            continue
        distance = round(distance, 3)
        print ('Distance : %f cm'%distance)

        if distance < 50:
            gpio.output(pin_vib, True)
        else :
            gpio.output(pin_vib, False)

        
except (KeyboardInterrupt, SystemExit):
    gpio.cleanup()
    sys.exit(0)
except:
    gpio.cleanup()