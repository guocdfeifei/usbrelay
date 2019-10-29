import copy

aab = 'A|2019-10-25 19:23:11|0|0                                                      '

# aa=['A', '2019-10-25 16:23:11', '0',1]
# num_list_new = [str(x) for x in aa]
# print(num_list_new)
# print('|'.join(num_list_new))


oplist = aab.split('|')
print('oplist',oplist)
newlist = copy.deepcopy(oplist)
#A
tmpstr1 = newlist[2].strip().strip(b'\x00'.decode())
print('tmpstr1',tmpstr1)
newlist[2] = int(tmpstr1)+1
#B
tmpstr = newlist[3].strip().strip(b'\x00'.decode())
print('tmpstr',tmpstr)
newlist[3] = int(tmpstr)+1