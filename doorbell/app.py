import RPi.GPIO as GPIO
import time
import requests
import yaml

config = yaml.safe_load(open("config.yml"))

GPIO.setmode(GPIO.BOARD)

buttonPin = 11
ledPin = 16

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
      print "On"

    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
