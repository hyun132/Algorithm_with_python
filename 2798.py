import sys
from itertools import combinations

N,M=sys.stdin.readline().split()
N=int(N)
M=int(M)

nums=list(map(int,sys.stdin.readline().split()))
sums=[]
for x,y,z in list(combinations(nums,3)):
    sum=x+y+z
    if sum<=M:
        sums.append(sum)

sums.sort()
print(sums[-1])
