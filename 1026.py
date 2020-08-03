import heapq
import sys

N=int(sys.stdin.readline().strip())

A=list(map(int,sys.stdin.readline().strip().split()))
B=list(map(int,sys.stdin.readline().strip().split()))

A.sort()
# B.sort(reverse=True)

def fun():
    sum=0
    for i in range(N):
        b=max(B)
        sum+=A[i]*b
        B.remove(b)
    print(sum)

fun()