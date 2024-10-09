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

gpio.setup(pin_lux, gpio.IN)
gpio.setup(pin_led, gpio.OUT)

time.sleep(0.5)

print ('LUX - LED TEST')

try :
    while True :
        if gpio.input(pin_lux) == True:
            gpio.output(pin_led, True)
        else :
            gpio.output(pin_led, False)

        
except (KeyboardInterrupt, SystemExit):
    gpio.cleanup()
    sys.exit(0)
except:
    gpio.cleanup()