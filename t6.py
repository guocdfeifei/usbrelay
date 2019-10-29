import os
dev='E:/'
oppath = os.path.join(dev, 'test.txt')
print('oppath',oppath)
oplast_line=''
with open(oppath, 'r') as f:  # 打开文件
    lines = f.readlines()  # 读取所有行
    first_line = lines[0]  # 取第一行
    last_line = lines[-1]  # 取最后一行
    print(first_line)
    print(last_line)
    oplast_line=last_line
newstr='A|2019-10-28 12:41:33|1|0'
with open(oppath, mode='a+', encoding="utf-8") as w:
            w.write("\n"+newstr.strip().strip(b'\x00'.decode()))