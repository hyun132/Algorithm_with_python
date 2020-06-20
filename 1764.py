import sys

n,m=map(int,sys.stdin.readline().split())
a=set()
for _ in range(n):
    a.add(sys.stdin.readline().strip())
b=set()
for _ in range(m):
    b.add(sys.stdin.readline().strip())

c=b&a

print(len(c))
for i in sorted(c):
    print(i)