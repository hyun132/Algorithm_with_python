import sys

sys.stdin.readline()
A=set(sys.stdin.readline().split())

sys.stdin.readline()
arr=list(sys.stdin.readline().split())
B=set(arr)

C=B&A
for i in arr:
    if i in C:
        print(1)
    else:
        print(0)


