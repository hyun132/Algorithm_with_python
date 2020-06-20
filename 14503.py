import sys

ysize,xsize=map(int,sys.stdin.readline().strip().split())

y,x,d=map(int,sys.stdin.readline().strip().split())

board=[list(map(int,sys.stdin.readline().strip().split())) for i in range(ysize)]

dirarr=[(0,-1),(-1,0),(0,1),(1,0)]
#  1 0  0 -1  -1 0  0 1
temp=0
for item in board:
    temp+=item.count(0)
cnt=0
result=1

visited=[[0]*xsize for _ in range(ysize)]
visited[y][x]=1
t=2

while True:
    dy,dx= dirarr[d]
    if 0<=y+dy<ysize and 0<=x+dx<xsize:
        if board[y+dy][x+dx]==0 and visited[y+dy][x+dx]==0:
            y += dy
            x += dx
            visited[y][x] = t
            t+=1
            result+=1
            cnt=0
        else:
            cnt+=1
            # print(d)
    else:
        cnt += 1
        # print(d)
    if d - 1 < 0:
        d = 3
    else:
        d -= 1
    if cnt<4:
        continue

    if d-1<0 : tempdir=3
    else : tempdir=d-1

    if 0<=y+dirarr[tempdir][0]<ysize and 0<=x+dirarr[tempdir][1]<xsize and board[y+dirarr[tempdir][0]][x+dirarr[tempdir][1]] !=1:
        y += dirarr[tempdir][0]
        x += dirarr[tempdir][1]
        cnt=0
    else:
        for i in range(ysize):
            print(visited[i])
        print(result)
        exit()
    if result >=temp:
        print(result)
        exit()












