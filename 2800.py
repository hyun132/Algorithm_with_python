import sys
from itertools import combinations

inputstr=sys.stdin.readline()
inputstr=' '+inputstr+' '
spacestr=str(inputstr)
spacestr=spacestr.replace('(',' ')
spacestr=spacestr.replace(')',' ')
arr1=[]
arr2=[]
spacestr.replace('[()]',' ')

for i in range(len(inputstr)):
    if inputstr[i]=='(':
        arr1.append(i)
    elif inputstr[i]==')':
        arr2.append(i)


pair=[]
# print(arr1)
# print(arr2)

size=len(arr1)
right=0
left=len(arr1)-1
while True:
    while True:
        if len(arr1)<1:
            break
        # print('l',left,right)
        # print(arr1[left], arr2[right])
        if arr1[left] < arr2[right]:
            pair.append((arr1[left],arr2[right]))
            arr2.remove(arr2[right])
            arr1.remove(arr1[left])
            break
        left-=1

    left=len(arr1)-1
    if len(arr2)<1:
        break


# print(pair)

result=dict()
result[spacestr.replace(' ','').strip()]=0
for i in range(1,len(pair)):
    tempstr = spacestr[:]
    for case in combinations(pair,i):
        tempstr=spacestr[:]
        # print(case)
        for j in range(len(list(case))):

            tempstr=tempstr[:case[j][0]]+'('+tempstr[case[j][0]+1:case[j][1]]+')'+tempstr[case[j][1]+1:]

        result[tempstr.replace(' ','').strip()]=0

result=sorted(result.keys())
for k in result:
    print(k)

