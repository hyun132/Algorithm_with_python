def solution(board):
    for y in range(1,len(board)):
        for x in range(1,len(board[0])):
            if board[y][x]>0:
                board[y][x] = min(board[y-1][x],board[y][x-1],board[y-1][x-1])+1

    answer=0
    for row in board:
        answer=max(answer,max(row))

    print(answer)
    return answer**2


# solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
solution([[0,0,1,1],[1,1,1,1]])