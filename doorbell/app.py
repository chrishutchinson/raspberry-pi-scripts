import RPi.GPIO as GPIO
import time
import requests
import yaml
import os
import sys

# Hello, this a comment

configFile = os.path.join(sys.path[0], 'config.yml')
config = yaml.safe_load(open(configFile))

GPIO.setmode(GPIO.BOARD)

buttonPin = config['buttonPin']
ledPin = config['ledPin']

GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, GPIO.LOW)

# Request details
url = config['makerUrl']

print "Listening for doorbell presses..."
try:
  while 1:
    if GPIO.input(buttonPin):
      GPIO.output(ledPin, GPIO.LOW)
    else:
      GPIO.output(ledPin, GPIO.HIGH)
      requests.post(url)
      time.sleep(5)
      print "On"

    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
