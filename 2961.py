import sys
from itertools import combinations

n=int(sys.stdin.readline().strip())

arr=[]

if n==1:
    s, b = list(map(int, sys.stdin.readline().split()))
    print(abs(s-b))
    exit()
for i in range(n):
    s,b=list(map(int,sys.stdin.readline().split()))
    arr.append((s,b))

result=[]
for i in range(n):
    if i == 0:
        for item in arr:
            result.append(abs(item[0]-item[1]))
        continue
    for lst in combinations(arr,i+1):
        ns = 1
        nb = 0
        for j in range(i+1):
            ns*=lst[j][0]
            nb+=lst[j][1]
        result.append((abs(ns-nb)))
        if ns==nb:
            print(0)
            exit()
print(min(result))