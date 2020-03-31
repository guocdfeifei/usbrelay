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

@route('/Relay', method="POST")
def Relay_Control():
  global Relay1,Relay2,Relay3,Relay4,Relay5,Relay6,Relay7,Relay8
  
  Relay1 = request.POST.get('Relay1')
  Relay2 = request.POST.get('Relay2')
  Relay3 = request.POST.get('Relay3')
  Relay4 = request.POST.get('Relay4')
  Relay5 = request.POST.get('Relay5')
  Relay6 = request.POST.get('Relay6')
  Relay7 = request.POST.get('Relay7')
  Relay8 = request.POST.get('Relay8')
  GPIO.output(Relay[0], int(Relay1))
  GPIO.output(Relay[1], int(Relay2))
  GPIO.output(Relay[2], int(Relay3))
  GPIO.output(Relay[3], int(Relay4))
  GPIO.output(Relay[4], int(Relay5))
  GPIO.output(Relay[5], int(Relay6))
  GPIO.output(Relay[6], int(Relay7))
  GPIO.output(Relay[7], int(Relay8))

  
run(host="0.0.0.0", port=8080)
 

