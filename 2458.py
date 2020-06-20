import sys
from collections import deque

n,m=list(map(int,sys.stdin.readline().strip().split()))

# graphU=dict()
# graphD=dict()
# # for i in range(1,n+1):
# #     graphU[i] =[]
# #     graphD[i] = []
# INF=9999999
# board=[[INF]*(n+1) for _ in range(n+1)]
# for i in range(m):
#     small,tall =list(map(int, sys.stdin.readline().strip().split()))
#     # graphU[small].append(tall)
#     # graphD[tall].append(small)
#     board[small][small]=0
#     board[tall][tall]=0
#     board[small][tall]=1
#
# for s in range(1,n+1):
#     for e in range(1,n+1):
#         if i==s: continue
#         for i in range(1,n+1):
#             board[s][e]=min(board[s][i]+board[i][e],board[s][e])
#
# cnt=0
# for i in range(1,n+1):
#     temp=1
#     for j in range(1,n+1):
#         if board[i][j]==INF and board[j][i]==INF:
#             temp=0
#             break
#     cnt+=temp
# for i in range(n):
#     print(board[i])
# print(cnt)

def fun(start,graph,visited):
    temp=0
    q=deque()
    q.append(start)
    visited[start]=True
    while q:
        node=q.popleft()
        for item in graph[node]:
            if visited[item]==False:
                visited[item]=True
                q.append(item)
                temp+=1

    return temp

graphU=dict()
graphD=dict()
for i in range(1,n+1):
    graphU[i] =[]
    graphD[i] = []
for i in range(1,n+1):
    graphU[i] =[]
    graphD[i] = []
# arr=[[] for _ in range(n+1)]
# arr=[[0]*(n+1) for _ in range(n+1) ]
tallarr=[0]*(n+1)
smallarr =[0]*(n+1)

for i in range(m):
    small,tall =list(map(int, sys.stdin.readline().strip().split()))
    graphU[small].append(tall)
    graphD[tall].append(small)

ans=0
for i in range(1,n+1):
    num=fun(i,graphD,[False]*(n+1))+fun(i,graphU,[False]*(n+1))
    if num>=n-1 : ans+=1

print(ans)
