#!/usr/bin/python
#######
# This program would generate Squence pulse train on GPIO 14 Pin 26 of P1
#######
import RPi.GPIO as GPIO
from time import sleep
import sys
import signal
import time

pulses_per_sec = 25
rate = 1.0/pulses_per_sec
print(rate)

def signal_handler(signal, frame):
  print
  GPIO.cleanup()
  sys.exit(0)

def lopper():
  while 1:
    for index in range(pulses_per_sec):
      GPIO.output(14,0)
      GPIO.output(14,1)
      sleep(rate)
    localtime = time.asctime( time.localtime(time.time()) )
    print "done sendind at :", localtime
      

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
signal.signal(signal.SIGINT,signal_handler)
print("Press Ctrl+c to Stop Pulse train")
lopper()
GPIO.cleanup()

