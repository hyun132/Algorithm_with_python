import sys
from collections import deque

graph=dict()
for j in range(int(sys.stdin.readline().strip())):
    graph[j+1]=set()
for i in range(int(sys.stdin.readline().strip())):
    a,b = map(int,sys.stdin.readline().strip().split())
    graph[a].add(b)
    graph[b].add(a)

q=deque()
visited=[1]
q.append(1)
while q:
    node=q.pop()
    for next in graph[node]:
        if next in visited:
            continue
        visited.append(next)
        q.append(next)

print(len(visited)-1)

