# def fib(n):
#     if n==0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# n=input()
# print(fib(int(n)))
import sys

n = int(sys.stdin.readline())


def fib(k):
    n = 0
    m = 1
    for i in range(2,k+1):
        if n>m:
            m=n+m
        else :
            n=m+n
    return n if n>m else m
print(fib(n))