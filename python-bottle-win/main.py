#!/usr/bin/python
# -*- coding:UTF-8 -*-
from ctypes import *
#pyinstaller -F  -w  main.py

#pyinstaller -F main.py
from bottle import *
# import RPi.GPIO as GPIO

#GPIO Pin
from ctypes import *

import time
Relay = [1, 2, 3, 4, 5, 6, 7,8]
class relayop():
    def __init__(self):
        self.dll = CDLL("usb_relay_device.dll")
        print(self.dll.usb_relay_init())
        self.aa = self.dll.usb_relay_device_enumerate()
        print('设备清单', self.aa)
        self.getRel()

    def getRel(self):
        # lib = cdll.LoadLibrary("./usb_relay_device.lib")
        self.bb = self.dll.usb_relay_device_open(self.aa)
        print('打开设备', self.bb)
# status = c_int(0)
# print('打开设备',dll.usb_relay_device_get_status(aa,byref(status)))
# print('status',status.value)
    def openall(self):
        print('打开所有',self.dll.usb_relay_device_open_all_relay_channel(self.bb))
    def open(self,num):
        flag = 1
        while flag ==1:
            print('self.bb',self.bb)
            self.getStatus()
            flag = self.dll.usb_relay_device_open_one_relay_channel(self.bb, num)
            print('打开', flag)
            if flag==1:
                self.getRel()
            else:
                self.getStatus()

        return flag
    def close(self,num):
        flag = 1
        while flag == 1:

            self.getStatus()
            flag = self.dll.usb_relay_device_close_one_relay_channel(self.bb, num)
            print('关闭', flag)
            if flag == 1:
                self.getRel()
            else:
                self.getStatus()
        return flag
    def getStatus(self):
        # global Relay
        # print('Relay',Relay)
        # for rel in Relay:
        status = c_int(0)
        flag= self.dll.usb_relay_device_get_status(self.bb, byref(status))
        if flag ==0:
            print('执行前设备状态',status )  # aa, byref(status)
            print('0status', status.value,'bin',bin(status.value))
            return bin(status.value)
        else:
            print('状态查询失败')
            return '状态查询失败'
# print('打开',dll.usb_relay_device_open_one_relay_channel(bb,1))
# for i in range(1,5):
#     # print('暂停1s')
#     time.sleep(1)
#     print('打开',i,dll.usb_relay_device_open_one_relay_channel(bb,i))
#
# for i in range(1,5):
#     # print('暂停1s')
#     time.sleep(1)
#     print('关闭',i,dll.usb_relay_device_close_one_relay_channel(bb,i))
    def closeall(self):
        # time.sleep(10)
        print('关闭所有',self.dll.usb_relay_device_close_all_relay_channel(self.bb))

# Relay = [2, 3, 25, 14, 15, 18, 23, 24]

# Relay = [8,7,6,5,4,3,2,1]
# Relay = [8,7,6,5,4,3,2,1]
# Relay = [22, 27, 17, 18, 15, 14, 3,2]
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
# GPIO.setmode(GPIO.BCM)
#
# for i in range(8):
#     GPIO.setup(Relay[i], GPIO.OUT)
#     opRelay(Relay[i], GPIO.HIGH)
#加载继电器
relay = relayop()
def opRelay(Relay, state):

  if state==0:
    relay.open(Relay)
  else:
    relay.close(Relay)



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
  # updateRelay(Relay[int(Relay1) - 1], int(RelayState))
  opRelay(Relay[int(Relay1) - 1], int(RelayState))
  # Relay1 = request.POST.get('Relay1')
  # Relay2 = request.POST.get('Relay2')
  # Relay3 = request.POST.get('Relay3')
  # Relay4 = request.POST.get('Relay4')
  # Relay5 = request.POST.get('Relay5')
  # Relay6 = request.POST.get('Relay6')
  # Relay7 = request.POST.get('Relay7')
  # Relay8 = request.POST.get('Relay8')
  #
  # # opRelay(Relay[0], int(Relay1))
  # opRelay(Relay[1], int(Relay2))
  # opRelay(Relay[2], int(Relay3))
  # opRelay(Relay[3], int(Relay4))
  # opRelay(Relay[4], int(Relay5))
  # opRelay(Relay[5], int(Relay6))
  # opRelay(Relay[6], int(Relay7))
  # opRelay(Relay[7], int(Relay8))

checkFlag=False

def checkmin():
    result = relay.getStatus()
    sleepmin = 10
    findstep = 1
    rennum = 5
    renbegin = 0
    print('result', result, type(result))
    subStatus = result[2:]
    print('subStatus', subStatus)
    while True:
        global checkFlag
        checkFlag = True
        while int(subStatus) != 0:
            print('有非0状态的继电器')
            renbegin = renbegin + 1
            print('忍了', renbegin)
            time.sleep(findstep)
            if renbegin > rennum:
                print('忍够了，要切换为初始状态')
                i = 0
                for rel in subStatus[::-1]:
                    i = i + 1
                    print(i, 'rel', rel, '准备重置为0状态')
                    relay.close(i)

            # else:
            result = relay.getStatus()
            print('result', result, type(result))
            subStatus = result[2:]
            print('subStatus', subStatus)
        print(sleepmin, '分钟后再检测')
        time.sleep(sleepmin * 60)

'''
内网 10分钟检查继电器状态，如果任意一个是吸合状态，1秒钟检测一次，连续五次一直吸合（高电压状态为吸合状态），发送断开吸合指令，保证所有继电器都是断开的
'''
@route('/RelayStatus', method="GET")
def Relay_Status():
    result=relay.getStatus()
    print('result',result,type(result))
    subStatus=result[2:]
    print('subStatus',subStatus)
    if not checkFlag:
        print('后台启动监控')

        t = threading.Thread(target=checkmin, args=())
        t.setDaemon(True)
        t.start()
        print('线程启动了')
    else:
        print('检测程序已启动了')


    return {'result': result}


print('后台启动监控')

t = threading.Thread(target=checkmin, args=())
t.setDaemon(True)
t.start()
print('线程启动了')
run(host="0.0.0.0", port=8080)
 

