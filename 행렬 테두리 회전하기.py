def solution(rows, columns, queries):

    board = [[j for j in range((y-1)*columns+1,y*columns+1)] for y in range(1,rows+1)]
    minarr=[]

    for query in queries:
        y1,x1,y2,x2 = query[0]-1,query[1]-1,query[2]-1,query[3]-1
        leftcol=[]
        rightcol=[]
        toprow=[]
        bottomrow=[]
        for i in range(y2 - y1 + 1):
            leftcol.append(board[y2 - i][x1])
            rightcol.append(board[y1 + i][x2])
            if i > 0 :
                board[y2 - i][x1] = leftcol[-2]
                board[y1 + i][x2] = rightcol[-2]

        toprow.append(leftcol[-1])
        bottomrow.append(rightcol[-1])

        for i in range(1,x2 - x1 + 1):
            toprow.append(board[y1][x1 + i])
            bottomrow.append(board[y2][x2 - i])
            board[y1][x1 + i] = toprow[-2]
            board[y2][x2 - i] = bottomrow[-2]
        minarr.append(min(min(leftcol),min(rightcol),min(toprow),min(bottomrow)))

    print(minarr)

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])
# solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
# solution(100,97,[[1,1,100,97]])