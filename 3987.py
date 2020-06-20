import sys
from collections import deque

def fun(y,x,dir):
    cnt=1
    ny,nx=dir
    while True:
        y, x = y + ny, x + nx
        if 0>y or y==n or 0>x or x==m or board[y][x]=='C':
            return cnt
        # print(y,x)
        # if board[y][x]=='C':
        #     return cnt
        if board[y][x]=='/':
            ny,nx=-nx,-ny
        elif board[y][x]=='\\':
            ny,nx=nx,ny
        cnt += 1

        if cnt>n*m:
            printdir(dir)
            print('Voyager')
            exit()

def printdir(dir):
    if dir == (-1, 0):
        print('U')
    elif dir == (0, 1):
        print('R')
    elif dir == (1, 0):
        print('D')
    else:
        print('L')

n,m=map(int,sys.stdin.readline().split())

board=[sys.stdin.readline().strip() for _ in range(n)]

# q=deque()
y,x=map(int,sys.stdin.readline().split())
# q.append((y,x))
# print(q)

d=[(-1,0),(0,1),(1,0),(0,-1)]
result=[]
for dir in d:
    result.append((fun(y-1,x-1,dir),dir))


# print(result)
result.sort(key=lambda x:x[0],reverse=True)
# print(result)

# for item in resu

printdir(result[0][1])
print(result[0][0])
# print(board)