import pygame
import RPi.GPIO as GPIO
import time
import threading

#ping 21 is pulled down
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
blinkLeds = False


def play_glory(channel):
    global blinkLeds
    if pygame.mixer.get_init() != None and pygame.mixer.music.get_busy() == True:
        pygame.mixer.quit()
        blinkLeds = False
    else:
        pygame.mixer.init()
        pygame.mixer.music.load("gloryglory.mp3")
        pygame.mixer.music.play()
        blinkLeds = True
        

#pin 21 will play the song on rising edge
GPIO.add_event_detect(21, GPIO.RISING, callback=play_glory, bouncetime=500)

while True:
    if blinkLeds:
        if pygame.mixer.get_init() != None and pygame.mixer.music.get_busy() == True:
            GPIO.output(22, 1)
            GPIO.output(23, 1)
            GPIO.output(24, 1)
            GPIO.output(25, 1)
            time.sleep(0.36)
            GPIO.output(22, 0)
            GPIO.output(23, 0)
            GPIO.output(24, 0)
            GPIO.output(25, 0)
            time.sleep(0.36)
        else:
            blinkLeds = False
    else:
        time.sleep(0.1)
