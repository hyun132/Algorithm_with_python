import sys
n,m=list(map(int,sys.stdin.readline().split()))
if n==1 and m==1:
    print(1)
    exit()
board=[]
for i in range(n):
    temparr=[]
    row=sys.stdin.readline().strip()
    for num in row:
        temparr.append(int(num))
    board.append(temparr)

in_x=[]
in_y=[]
sqare=[1]
nx=0
ny=0
for y in range(n):
    for x in range(m):
        start=board[y][x]
        for nx in range(m-1,x,-1) :
            if board[y][nx]==start:
                # print(y,nx)
                if y+nx-x<n:
                    if board[y+nx-x][x]==start and board[y+nx-x][nx]==start:
                        # print(nx)
                        sqare.append((nx-x+1)**2)
        # for ny in range(n-1,y,-1):
        #     if board[ny][x] == start:
        #         in_y.append(ny)
        # print(in_x)
        # print(in_y)
        # if len(in_x) != 0 and len(in_y) != 0:
        #     for dx in in_x:
        #         for dy in in_y:
        #             if dx==dy:
        #                 if board[dy][dx]==start:
        #                     sqare.append((dx-x+1) * (dy-y+1))
        #                     print((dx-x+1) * (dy-y+1))
        # else:
        #     sqare.append(1)
        # in_x = []
        # in_y = []

print(max(sqare))