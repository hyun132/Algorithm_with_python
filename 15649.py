import sys
import operator
from itertools import permutations

n,m=map(int,sys.stdin.readline().split())

a=b=1

for i in range(1,max(m,n-m)+1):
    a=operator.mul(a,n+1-i)
#     b=operator.mul(b,i)
# case=operator.floordiv(a,b)
case = a
# print(case)

arr = [i for i in range(1,n+1)]

result=[]
row=[]

count=0
for i in permutations(arr,m):
    for j in i:
        print(j, end=' ')
    count += 1
    if count != case:
        print()
# for i in range(len(case)):
#     for j in case[i]:
#         print(i,end=' ')
#     if i!= len(case):
#         print()
    # result.append(row)
    # print(result)
# for i in result:
#     print(i)
