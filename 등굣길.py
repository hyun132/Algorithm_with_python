def solution(m, n, puddles): #m이 x n 이 y

    board=[[0]*(m+1) for _ in range(n+1)]
    board[1][1]=1

    for y in range(1,n+1):
        for x in range(1,m+1):
            if (y==1 and x==1) or [x,y] in puddles:
                continue
            else:
                board[y][x]=board[y-1][x]+board[y][x-1]

    # for r in board:
    #     print(r)
    print(board[n][m]%1000000007)
    return board[n][m]%1000000007


# solution(4,3,[[2,2]])

# solution(5,1,[[1,5]])

solution(100,20,[[15,15],[15,16]])