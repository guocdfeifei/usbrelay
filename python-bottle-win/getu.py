#author=guoff
#date  18:04
import subprocess
import os
import re


def sh(command, print_msg=True):
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('gbk')#utf-8
    if print_msg:
        print(result)
    return result


def usbpath():
    if os.name == 'nt':
        disks = sh("wmic logicaldisk get deviceid, description",
                   print_msg=False).split('\n')
        for disk in disks:
            if 'Removable' in disk:
                return re.search(r'\w:', disk).group()
    elif os.name == 'posix':
        return sh('ll -a /media')[-1].strip()
    else:
        return sh('ls /Volumes')[-1].strip()


print(usbpath())