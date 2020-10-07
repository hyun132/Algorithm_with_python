from sys import stdin

K,N = map(int,stdin.readline().strip().split())
lans=(int(stdin.readline().strip()))
# lans=list(map(int,stdin.readlines()))
s=1
e=max(lans)

while s <= e:
    m=(s+e)//2
    sticks=sum([line//m for line in lans])
    if sticks>=N:
        s=m+1
        result = m
    else:
        e=m-1
print(result)