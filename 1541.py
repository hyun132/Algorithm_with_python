import sys
from collections import deque

string=sys.stdin.readline().strip().split('-')

arr=deque()
temp=0
for i in string:
    for j in i.split('+'):
        temp=temp+int(j)
    arr.append(temp)
    temp = 0

result=arr[0]
for i in range(1,len(arr)):
    result=result-arr[i]
print(result)

# while True:
#     # print(arr)
#     a=arr.pop()
#     op=arr.pop()
#     if op =='+':
#         a=a+arr.pop()
#         arr.append(a)
#     elif op=='-':
#         sum+=int(-a)
#     if len(arr)<2:
#         sum=sum+arr.pop()
#         print(sum)
#         break
    # print(arr)
# sum=0
# for i in temparr:
#     sum=sum+i
# print(sum)
