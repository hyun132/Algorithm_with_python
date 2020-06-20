from collections import deque
n,m = map(input().split())
board=[list(map(int,list(input))) for _ in range(n)]
q=deque()

visited=[[False]*m for _ in range(n)]
count=[[0]*m for _ in range(n)]

count[0][0]=1
visited[0][0]=True
q.append((0,0))
while q:
    x,y = q.popleft()
    dn=[(0,1),(0,-1),(1,0),(-1,0)]

    for dx,dy in dn:
        if 0<=x+dx<n and 0<=y+dy<m:
            if board[x+dx][y+dy]==1 and (x+dx,y+dy) not in visited:
                q.append((x+dx,y+dy))
                visited[x+dx][y+dy]=True
                count[x+dx][y+dy]=count[x][y]+1

print(count[n-1][m-1])