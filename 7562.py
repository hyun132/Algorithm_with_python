import sys
from collections import deque

case=int(sys.stdin.readline().strip())

for _ in range(case):
    boardsize=int(sys.stdin.readline().strip())
    sy,sx=list(map(int,sys.stdin.readline().split()))
    ey,ex=list(map(int,sys.stdin.readline().split()))
    # print(sy,sx,ey,ex)
    board=[[False for _ in range(boardsize)] for i in range(boardsize)]

    q=deque()
    q.append((sy,sx))
    board[sy][sx]=1
    d=[(-2,-1),(-2,1),(-1,2),(1,2),(-1,-2),(1,-2),(2,-1),(2,1)]
    cnt=0
    result=0
    while q:
        qsize=len(q)
        cnt+=1
        for i in range(qsize):
            ny,nx=q.popleft()
            for dy,dx in d:
                y,x=dy+ny,dx+nx
                if y==ey and x==ex:
                    board[y][x] = cnt
                    result=cnt
                    break
                if 0<=y<boardsize and 0<=x<boardsize and board[y][x]==False:
                    q.append((y,x))
                    board[y][x]=cnt

            if board[ey][ex] != False:
                break
        if board[ey][ex]!=False:
            break
    print(result)