import sys
from collections import deque

case = int(sys.stdin.readline().strip())


def bfs(board,Y,X,ysize,xsize):
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((Y,X))
    board[Y][X]=0

    while q:
        ny,nx = q.popleft()
        for dy,dx in d:
            if 0<=ny+dy<ysize and 0<=nx+dx<xsize and board[ny+dy][nx+dx]==1:
                q.append((ny+dy,nx+dx))
                board[ny + dy][nx + dx] = 0
    return 1

for term in range(case):
    cnt=0
    X,Y,k = list(map(int,sys.stdin.readline().strip().split()))
    if k==0:
        print(0)
        break

    board = [[0 for _ in range(X)] for _ in range(Y)]
    for i in range(k):
        x, y = list(map(int, sys.stdin.readline().strip().split()))
        board[y][x] = 1

    for yy in range(Y):
        for xx in range(X):
            if board[yy][xx]==1:
                cnt+=bfs(board,yy,xx,Y,X)

    print(cnt)


