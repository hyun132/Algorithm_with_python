import sys


def fun(start, dir):
    sy, sx = start
    dy, dx = dir
    # n=len(board)
    if 0 <= sy + dy < n+2 and 0 <= sx + dx < n+2:
        ny, nx = sy + dy, sx + dx
        if board[ny][nx] == 1:
            if dir == (-1, 0):
                fun((ny, nx), (0, 1))
            elif dir == (0, 1):
                fun((ny, nx), (1, 0))
            elif dir == (1, 0):
                fun((ny, nx), (0, -1))
            else:
                fun((ny, nx), (-1, 0))
        else:
            fun((ny, nx), dir)
    else:
        print(sy,sx)


case = int(sys.stdin.readline().strip())

for i in range(case):
    n,r= list(map(int,sys.stdin.readline().split()))
    # print(n,r)
    board=[[0]*(n+2) for _ in range(n+2)]

    for j in range(r):
        y,x=list(map(int,sys.stdin.readline().split()))
        board[y][x]=1

    ly,lx=list(map(int,sys.stdin.readline().split()))
    start=(ly,lx)
    # dir = [(-1, 0), (-1, 0), (-1, 0), (-1, 0)]

    if ly==0:
        fun(start,(1,0))
    elif ly==n+1:
        fun(start,(-1,0))
    else:
        if lx==0:
            fun(start,(0,1))
        elif lx==n+1:
            fun(start,(0,-1))

    # for d in dir:
    #     fun((ly,lx),d)
