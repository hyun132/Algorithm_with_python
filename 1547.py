import sys

M=int(sys.stdin.readline().strip())

arr=[0,1,0,0]
for i in range(M):
    X,Y=list(map(int,sys.stdin.readline().strip().split()))

    if arr[X]==1:
        arr[X]=0
        arr[Y]=1
    elif arr[Y]==1:
        arr[Y]=0
        arr[X]=1

print(arr.index(1))
