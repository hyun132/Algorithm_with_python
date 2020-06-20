import sys
from collections import deque
def dfs(i,j):
    board[i][j]=0
    q = deque()
    q.append((i, j))
    while q:
        nx,ny=q.popleft()
        dn=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        for dx,dy in dn:
            x=nx+dx
            y=ny+dy
            if 0<=x<m and 0<=y<n:
                if board[x][y]==1 and (x,y) not in q:
                    board[x][y]=0
                    q.append((x,y))

while True:
    n,m=map(int,sys.stdin.readline().split())
    if n==0 and m==0: break
    board=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]
    visited=[[False]*m for _ in range(n)]
    count=0

    for i in range(m):
        for j in range(n):
            if board[i][j]==1:
                dfs(i,j)
                count+=1
    print(count)



