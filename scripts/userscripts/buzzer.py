#!/usr/bin/env python3
########################################################################
# Filename    : Doorbell.py
# Description : Make doorbell with buzzer and button
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

class Buzzer:
    buzzerPin = None
    def __init__(self, buzzerBoardPin):
        self.buzzerPin = buzzerBoardPin
        GPIO.setmode(GPIO.BOARD)        # use BCM GPIO Numbering
        GPIO.setup(self.buzzerPin, GPIO.OUT)   # set buzzerPin to OUTPUT mode

    def beep(self, duration):
        GPIO.output(self.buzzerPin,GPIO.HIGH) # turn on buzzer
        time.sleep(duration)
        GPIO.output(self.buzzerPin,GPIO.LOW) # turn on buzzer


    def cleanup(self):
        GPIO.cleanup()                     # Release all GPIO

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    buz = Buzzer(15)
    try:
        buz.beep(0.01)
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        bug.cleanup()
