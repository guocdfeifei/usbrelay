#!/usr/bin/python
# -*- coding:UTF-8 -*-

from bottle import *
import RPi.GPIO as GPIO

#GPIO Pin
Relay = [2, 3, 14, 15, 18, 17, 27, 22]

#All the relay
Relay1 = 1
Relay2 = 1
Relay3 = 1
Relay4 = 1
Relay5 = 1
Relay6 = 1
Relay7 = 1
Relay8 = 1

#GPIO init
GPIO.setmode(GPIO.BCM)

for i in range(8):
    GPIO.setup(Relay[i], GPIO.OUT)
    GPIO.output(Relay[i], GPIO.HIGH)

@get("/")
def index():
  global Relay1,Relay2,Relay3,Relay4,Relay5,Relay6,Relay7,Relay8
  
  Relay1 = 1
  Relay2 = 1
  Relay3 = 1
  Relay4 = 1
  Relay5 = 1
  Relay6 = 1
  Relay7 = 1
  Relay8 = 1
  
  return static_file('index.html', './')

@route('/<filename>')
def server_Static(filename):
    return static_file(filename, root='./')

def updateRelay(relay,state):
    before = GPIO.input(relay)
    flag=True
    while flag and before!=state:
        GPIO.output(relay, int(state))
        after = GPIO.input(relay)
        if before!=after:
            flag=False

@route('/Relay', method="POST")
def Relay_Control():
  global Relay1,Relay2,Relay3,Relay4,Relay5,Relay6,Relay7,Relay8
  
  Relay1 = request.POST.get('Relay')
  RelayState = request.POST.get('RelayState')
  updateRelay(Relay[int(Relay1)-1], int(RelayState))

  
run(host="0.0.0.0", port=8080)
 

