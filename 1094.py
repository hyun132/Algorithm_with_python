import sys

x=int(sys.stdin.readline().strip())

arr = [2**i for i in range(6,-1,-1)]

idx=0
cnt=0
while x>0:
    if x>=arr[idx]:
        x=x-arr[idx]
        cnt+=1
    else:
        idx+=1
        if idx == len(arr):
            break

print(cnt)




