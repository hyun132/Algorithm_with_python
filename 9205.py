import sys
from collections import deque

t=int(sys.stdin.readline().strip())

result=[[] for _ in range(t)]
for c in range(t):
    n = int(sys.stdin.readline().strip())
    start=list(map(int,sys.stdin.readline().split()))

    point=[]
    for i in range(n):
        point.append(list(map(int,sys.stdin.readline().split())))

    end =list(map(int,sys.stdin.readline().split()))
    point.append(end)

    visited=[False for _ in range(n+1)]

    q=deque()
    q.append(start)

    flag=0
    while q:
        start=q.pop()
        if start==end:
            flag=1
            print("happy")
            break
        for i in range(len(point)):
            if visited[i]!=True:
                dx,dy=point[i]
                if abs(start[0]-dx)+abs(start[1]-dy)<=1000:
                    q.append([dx,dy])
                    visited[i]=True

    if flag==0:
        print("sad")

