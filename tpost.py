import json

import requests
import time


def testpost():
    indata = {
    "DEPARTMENT": "140601",
    "FANNUM": 140601001,
    "FAULTDESC": "风速功率不匹配故障1",
    "FAULTNUM": "133",
    "FINDDATE": "2019-10-9 12:12:11",
    "UUID": "050"
}

    inparm = json.dumps(indata)
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post( 'http://10.72.64.220:8000/OmsWarning/',data=inparm)
    print('r', r.text)
    # print(r.content.decode('utf-8', errors="replace"))
    qunfainfo = json.loads(r.text)
    print('qunfainfo',qunfainfo)


def dqpost():
    timestruct = time.localtime()
    finddate = time.strftime('%Y-%m-%d %I:%M:%S', timestruct)

    indata = {
    "DEPARTMENT": 140623999,
    "FANNUM": "JD7X.Bool.Rd.b0.1255",
    "TYPE": "1",
    "FAULTDESC": "35kV集电II线零流I段保护动作314开关跳闸",
    "FAULTNUM": "131",
    "FINDDATE": finddate,
    "UUID": "050"
     }

    inparm = json.dumps(indata)
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post( 'http://10.72.64.220:8000/OmsDqWarning/',data=inparm)#127.0.0.1 10.72.64.220
    print('r', r.text)
    # print(r.content.decode('utf-8', errors="replace"))
    qunfainfo = json.loads(r.text)
    print('qunfainfo',qunfainfo)

# testpost()
dqpost()