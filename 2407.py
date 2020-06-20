import math
import sys
import operator

n,m=map(int,sys.stdin.readline().split())

r=min(m,n-m)
if n==m:
    print(1)
else:
    a=b=1
    for i in range(n,n-r,-1):
        a=operator.mul(a, i)
    for j in range(1,r+1):
        b=operator.mul(b,j)
print(operator.floordiv(a, b))