import sys
from collections import deque

F,S,G,U,D=list(map(int,sys.stdin.readline().split()))
q=deque()
q.append(S)

visited=[False for _ in range(F+1)]
flag=0


if G==S:
    print(0)
    exit()
# if U==D and G%U==S:
#     print("use the stairs")
#     exit()

cnt=-1
visited[S]=True
while q:
    cnt+=1
    size=len(q)
    for _ in range(size):
        start=q.popleft()
        if start==G:
            flag=1
            print(cnt)

        if 0<start+U<=F:
            if visited[start+U]==False:
                q.append(start+U)
                visited[start+U]=True
        if 0 < start - D <= F:
            if visited[start-D]==False:
                q.append(start-D)
                visited[start-D]=True
if flag==0:
    print("use the stairs")

