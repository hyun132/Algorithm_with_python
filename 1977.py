import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

max=int(N**0.5)
min=int(M**0.5)

sum=0
lastitem=0
for i in range(max,min-1,-1):
    if i*i>=M:
        sum=sum+i*i
        lastitem=i*i
if sum!= 0 :
    print(sum)
    print(lastitem)
else:
    print(-1)