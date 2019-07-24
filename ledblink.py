#import libraries
import RPi.GPIO as GPIO
import time
 
#set GPIO numbering mode and blah blah blah
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

#blink dem LED tings 
for x in range(0,10):
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,False)
    time.sleep(.5)
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,False)
    time.sleep(.5)
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,True)
    time.sleep(.5)
  

#clean dem GPIO pin tings
GPIO.cleanup()
