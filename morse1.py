import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    #Ham Radio is for losers
    
    #H
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #A
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #M
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of word
    GPIO.output(18, False)
    time.sleep(1.2)
    
    
    #R
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)    
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #A
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #D
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #I
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #O
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of word
    GPIO.output(18, False)
    time.sleep(1.2)
    
    #I
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    #S
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of word
    GPIO.output(18, False)
    time.sleep(1.2)
    
    
    #F
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter    
    GPIO.output(18, False)
    time.sleep(0.4)
    #O
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)    
    #R
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)    
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of word
    GPIO.output(18, False)
    time.sleep(1.2)


    #L
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)   
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #O
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #S
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #E
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #R
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dash
    GPIO.output(18, True)
    time.sleep(0.6)
    GPIO.output(18, False)
    time.sleep(0.2)    
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #end of letter
    GPIO.output(18, False)
    time.sleep(0.4)
    
    #S
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)
    #dot
    GPIO.output(18, True)
    time.sleep(0.2)
    GPIO.output(18, False)
    time.sleep(0.2)    
    #end of word
    GPIO.output(18, False)
    time.sleep(1.2)

    #end of sentence
    GPIO.output(18, False)
    time.sleep(1.2)