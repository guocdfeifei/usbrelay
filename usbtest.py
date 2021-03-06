import copy
import os
import shutil

import datetime
import psutil

import time,sys

# from win32gui import MessageBox as box
#pyinstaller -F usbtest.py

#/*

# *  ---全局数据 实时更新

# */
from t1 import relayop

local_device = []                   #本地驱动器

local_letter = []                   #本地盘符

local_number = 0                    #本地驱动器数


mobile_device = []                  #移动设备

mobile_letter = []                  #移动设备盘符

mobile_number = 0                   #移动设备数


def updata():
    global local_device, local_letter, local_number, \
        mobile_device, mobile_letter, mobile_number


    # 引入全局变量


    tmp_local_device, tmp_local_letter = [], []

    tmp_mobile_device, tmp_mobile_letter = [], []

    tmp_local_number, tmp_mobile_number = 0, 0

    try:

        part = psutil.disk_partitions()

    except:

        print("程序发生异常!!!")

        print(None, "很抱歉，程序发生了异常", "致命错误", 0)

        sys.exit(-1)

    else:

        # * 驱动器分类

        for i in range(len(part)):

            tmplist = part[i].opts.split(",")
            # print('tmplist',tmplist,len(tmplist)) len(tmplist)>1 and
            if  len(tmplist)>1 and tmplist[1] == "fixed":  # 挂载选项数据内读到fixed = 本地设备

                tmp_local_number = tmp_local_number + 1

                tmp_local_letter.append(part[i].device[:2])  # 得到盘符信息

                tmp_local_device.append(part[i])

            else:

                tmp_mobile_number = tmp_mobile_number + 1

                tmp_mobile_letter.append(part[i].device[:2])

                tmp_mobile_device.append(part[i])

        # *浅切片

        local_device, local_letter = tmp_local_device[:], tmp_local_letter[:]

        mobile_device, mobile_letter = tmp_mobile_device[:], tmp_mobile_letter[:]

        local_number, mobile_number = tmp_local_number, tmp_mobile_number

    return len(part)  # 返回当前驱动器数


def print_device(n):
    global local_device, local_letter, local_number, \
     \
            mobile_device, mobile_letter, mobile_number


    print("=" * 50 + "\n读取到" + str(n) + "个驱动器")

    for l in range(local_number):
        print(local_letter[l], end="")  # 列出本地驱动器盘符

    print("{" + local_device[0].opts + "}")

    if (len(mobile_device)):  # 列出移动驱动器盘符

        for m in range(mobile_number):
            print(mobile_letter[m], end="")

        print("{" + mobile_device[0].opts + "}")

    else:

        None

    print("进程进入监听状态 " + "*" * 10)

    return

import sys

print('参数个数为:', len(sys.argv), '个参数。')
print('参数列表:', str(sys.argv))



if __name__ == "__main__":
    '''
    记录电脑（AB）|时间|A次数|B次数
    A|2019-10-25 19:23:11|0|0
    '''
    #*初次读取驱动器信息，打印驱动器详细
    print('121212')
    now_number = 0                  #实时驱动数

    before_number = updata()        #更新数据之前的驱动数

    print_device(before_number)

    relay = relayop()
    now1state=False
    # if 'A' in sys.argv[1]:
    #     relay.close(1)
    #     relay.open(2)
    #     # time.sleep(1)
    #     # relay.open(1)
    #     # now1state = True
    #     time.sleep(3)
    #     #
    #     # relay.close(1)
    #     # time.sleep(60)
    # else:
    #     relay.close(1)
    #     relay.close(2)

    errcount=0
    waitcount=0
    while True:
        waitcount = waitcount+1

        # if waitcount>60:
        #     if 'A' in sys.argv[1]:
        #         print('60s停顿，重启继电器')
        #         relay.close(2)
        #         # relay.close(1)
        #         #更新磁盘数目
        #         time.sleep(3)
        #         before_number =  updata()
        #         time.sleep(5)
        #         relay.open(2)
        #         # relay.close(1)
        #         # time.sleep(3)
        #
        #         # relay.open(1)
        #         # time.sleep(3)
        #
        #         # relay.close(1)
        #         time.sleep(60)
        #         waitcount = 0

        # try:
        now_number = updata()
        # except Exception as e:
        #     estr = str(e)
        #     print('Error:', estr)
        #     time.sleep(5)
        #     errcount = errcount+1
        #     if errcount>6:
        #         print('60s停顿，重启继电器')
        #         if 'A' in sys.argv[1]:
        #             print('A，重启继电器')
        #             relay.close(2)
        #             time.sleep(3)
        #             before_number = updata()
        #             time.sleep(3)
        #             relay.open(2)
        #             time.sleep(3)
        #         else:
        #             print(sys.argv[1],'，重启继电器')
        #             relay.open(2)
        #             time.sleep(3)
        #             before_number = updata()
        #             time.sleep(3)
        #             relay.close(2)
        #             time.sleep(3)
        #         # if 'A' in sys.argv[1]:
        #         #     relay.close(1)
        #         #     relay.open(2)
        #         #     # time.sleep(1)
        #         #     # relay.open(1)
        #         #     now1state = False
        #         #     time.sleep(3)
        #         #     #
        #         #     # relay.close(1)
        #         #     # time.sleep(60)
        #         # else:
        #         #     relay.close(1)
        #         #     relay.close(2)
        #         #     now1state = False
        #         continue
        #         # elif 'B' in sys.argv[1]:
        #         # break
        #     else:
        #         # if now1state:
        #         #     relay.close(1)
        #         #     relay.open(1)
        #         #     # now1state = False
        #         #     # relay.close(1)
        #         # else:
        #         #     relay.open(1)
        #         #     relay.close(1)
        #             # now1state = True
        #         continue


        if(now_number > before_number):
            waitcount = 0
            print("检测到移动磁盘被插入...")
            time.sleep(1)
            print_device(now_number)

            print(None,"移动磁盘被插入\n","新插入磁盘",0)
            dev = mobile_device[-1].device
            print('mobile_device',mobile_device,dev)

                # w.write(str + "\n")


            before_number = now_number                  #刷新数据
            # time.sleep(10)
            # 追加写入到指定文件
            # str = "abcd"
            oppath = os.path.join(dev, 'test.txt')
            print('oppath',oppath)
            #查询文件是否存在，存在则转存到当前目录下的files文件夹下
            datetimenowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')  # 现在
            # begin_date = datetime.datetime.strptime(datetimenowTime, "%Y-%m-%d%H:%M:%S")
            new_name = "test" + datetimenowTime + ".txt"
            newpath=''
            # new_name =
            # if os.path.exists(oppath):
            #     #拷贝
            #     cmd = os.getcwd()
            #     if not os.path.exists(os.path.join(cmd,'files')):
            #         os.mkdir(os.path.join(cmd,'files'))
            #     newpath = os.path.join(cmd,'files',new_name)
            #     shutil.copyfile(oppath, newpath)
            # else:
            #     print('不存在文件',oppath)

            oplast_line=''

            while True:
                # if not os.path.exists(newpath):
                #     print('文件不存在等待2秒')
                #     time.sleep(5)
                #     break
                # else:
                #     break
                if os.path.exists(oppath):
                    # 拷贝
                    cmd = os.getcwd()
                    if not os.path.exists(os.path.join(cmd, 'files')):
                        os.mkdir(os.path.join(cmd, 'files'))
                    newpath = os.path.join(cmd, 'files', new_name)
                    shutil.copyfile(oppath, newpath)
                    break
                else:
                    print('不存在文件,休息5秒再检测', oppath)
                    time.sleep(5)
            print('newpath',newpath)
            with open(newpath, 'r') as f:  # 打开文件
                lines = f.readlines()  # 读取所有行
                first_line = lines[0]  # 取第一行
                last_line = lines[-1]  # 取最后一行
                print(first_line)
                print(last_line)
                oplast_line=last_line
            #操作最后一行
            oplist = oplast_line.split('|')
            print('oplist',oplist)
            newlist = copy.deepcopy(oplist)
            nowdev = sys.argv[1]
            print('nowdev',nowdev)
            newlist[0]=nowdev
            #取当前时间
            nowtime1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            newlist[1] =nowtime1
            if 'A' in nowdev:
                tmpstr1 = newlist[2].strip().strip(b'\x00'.decode())
                print('tmpstr1',tmpstr1)
                newlist[2] = int(tmpstr1)+1
            if 'B' in nowdev:
                tmpstr = newlist[3].strip().strip(b'\x00'.decode())
                print('tmpstr',tmpstr)
                newlist[3] = int(tmpstr)+1
            num_list_new = [str(x).strip().strip(b'\x00'.decode()) for x in newlist]
            newstr='|'.join(num_list_new)
            print('newlist',newlist,newstr)
            with open(newpath, mode='a+', encoding="utf-8") as w:
                w.write("\n"+newstr.strip().strip(b'\x00'.decode()))
                print('完成写操作',newstr,'操作后：',newstr.strip().strip(b'\x00'.decode()))
            print('完成写',newpath,'准备拷贝')
            shutil.copyfile(newpath,oppath)
            print('拷贝完成1')
            # time.sleep(5)
            print('拷贝完成2')
            #提出开关
            # relay.open(1)

            # if now1state:
            flag0 = relay.open(1)
            time.sleep(1)
            flag1 = relay.close(1)
            while flag0==1 or flag1==1:
                time.sleep(1)
                relay = relayop()
                flag0 = relay.open(1)
                time.sleep(1)
                flag1 = relay.close(1)

            # now1state=False
                # relay.close(1)
            # else:
            #     relay.open(1)
            #     now1state = True
                # relay.close(2)
            time.sleep(1)

        elif(now_number < before_number):

            print("检测到移动磁盘被拔出...")

            print_device(now_number)

            print(None,"移动磁盘被拔出\n","磁盘被拔出",0)

            before_number = now_number

            time.sleep(1)


