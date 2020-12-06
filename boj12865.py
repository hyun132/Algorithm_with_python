n,k = map(int,input().split())

board=[[0]*(k+1) for _ in range(n+1)]

for y in range(1,n+1):
    w,v=map(int,input().split())
    for x in range(1,k+1):
        if x>=w:
            board[y][x]=max(board[y-1][x-w]+v,board[y-1][x])
        else:
            board[y][x]=board[y-1][x]
# print(board)
print(board[-1][-1])
