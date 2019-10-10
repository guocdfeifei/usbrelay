from ctypes import *

import time

dll = CDLL("usb_relay_device.dll")
# lib = cdll.LoadLibrary("./usb_relay_device.lib")
print(dll.usb_relay_init())
aa = dll.usb_relay_device_enumerate()
print('设备清单',aa)
bb = dll.usb_relay_device_open(aa)
print('打开设备',bb)
# status = c_int(0)
# print('打开设备',dll.usb_relay_device_get_status(aa,byref(status)))
# print('status',status.value)
# print('打开所有',dll.usb_relay_device_open_all_relay_channel(bb))
# print('打开',dll.usb_relay_device_open_one_relay_channel(bb,1))
for i in range(1,5):
    # print('暂停1s')
    time.sleep(1)
    print('打开',i,dll.usb_relay_device_open_one_relay_channel(bb,i))

for i in range(1,5):
    # print('暂停1s')
    time.sleep(1)
    print('关闭',i,dll.usb_relay_device_close_one_relay_channel(bb,i))

# time.sleep(10)
# print('关闭所有',dll.usb_relay_device_close_all_relay_channel(bb))