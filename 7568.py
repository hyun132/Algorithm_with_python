import sys
from itertools import combinations

N=int(sys.stdin.readline())
rank=[1 for i in range(N)]
arr=[]
for i in range(N):
    W,H=map(int,sys.stdin.readline().split())
    arr.append([W,H])

for i in range(N):
    for j in range(N):
        if arr[i][0]>arr[j][0] and arr[i][1]>arr[j][1]:
            rank[j]+=1
for i in rank:
    print(i)
