import sys
from collections import deque


def fun(graph,startnode):
    # visited=[False for _ in range(N)]
    cost=[0]+[0 for _ in range(max(graph.keys()))]
    q=deque()
    q.append(startnode)
    # d=1
    while q:
        # size=len(q)
        node = q.popleft()
        flag=0
        for next in graph[node]:
            if cost[next]==0:
                cost[next]=cost[node]+1
                q.append(next)

                # elif cost[next]>d:
                #     cost[next] = d
    # print(cost)
    # print(sum(cost))
    return sum(cost)

N,M=map(int,sys.stdin.readline().split())

graph=dict()
for i in range(M):
    a,b= map(int,sys.stdin.readline().split())
    if a not in graph:
        graph[a]={b}
    else:
        graph[a].add(b)
    if b not in graph:
        graph[b]={a}
    else:
        graph[b].add(a)

# print(graph)
result=[]
for i in graph.keys():
    result.append((fun(graph,i),i))
# print(result)

# print(result)
result.sort()
# if M==1:
#     print(1)
# else:
# print(result)
print(result[0][1])