import json

import suds

from suds.client import Client

url = "http://10.1.3.45:7003/meaweb/wsdl/WARNINGSERVICE.wsdl"
client = suds.client.Client(url)
print(client)
# getHealthyHeBei是webService提供的方法
myjson={"data": [
        {
            "DEPARTMENT": "140604",
            "FANNUM": "140604082",
            "FAULTDESC": "(121)2#变桨子站总线异常",
            "FAULTNUM": "121",
            "FINDDATE": "2019-11-08 14:04:14",
            "TYPE": "0",
            "UUID": "050"
        }
    ]
}

inparm = json.dumps(myjson)
print(type(myjson),'type',type(inparm),inparm)
# data = bytes(inparm, 'utf8')
jsonstr = '''
{'data': [
        
    ]
}
'''
result = client.service.insertWarning(jsonstr)
# #
# # # 打印出结果
print(result)