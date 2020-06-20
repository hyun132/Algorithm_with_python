import sys

str=sys.stdin.readline().lower().strip().split()

if len(str[0])==1:
    print(str[0].upper())
    exit()

strarr=[]
for i in range(len(str[0])):
    strarr.append(str[0][i])

setstr=set(strarr)

sum=dict()
for i in setstr:
    sum[i]=0
#
for i in strarr:
    sum[i]+=1

list=sorted(sum.items(),key= lambda x :x[1],reverse=True)
#
# print(list)
if list[0][1]==list[1][1]:
    print('?')
else:
    char=list[0][0]
    print(char.upper())