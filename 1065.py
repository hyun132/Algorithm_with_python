#110 -> 99
import sys

N= int(sys.stdin.readline().strip())

cnt=0
if N <= 110:
    if N<99 :
        cnt=N
    else:
        cnt=99

else:
    for num in range(111,N+1):
        num=str(num)
        A=int(num[1]) - int(num[0])
        B=int(num[2]) - int(num[1])
        if A == B:
            cnt+=1

    cnt+=99
    # print(cnt)

print(cnt)