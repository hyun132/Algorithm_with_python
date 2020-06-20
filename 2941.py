import re
import sys

inputstr=sys.stdin.readline().strip()
# print(type(inputstr))
result=[]
# while inputstr!='':
    # inputstr.replace('c=','',1)
chars=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0
# while inputstr!='':
for item in chars:
    result.extend(re.findall(item,inputstr))
    inputstr=inputstr.replace(item,'.')
# print(result)
# print(len(result))
# inputstr.strip()
print(inputstr)

print(len(inputstr))