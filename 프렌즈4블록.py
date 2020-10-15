import copy


def solution(m, n, board):

    count=0

    newBoard=[]
    for row in board:
        newBoard.append([ch for ch in row])

    board=newBoard
    while True:
        toRemove = set()
        for y in range(m-1,0,-1):
            for x in range(n-1,0,-1):
                if board[y][x]==board[y-1][x-1]==board[y][x-1]==board[y-1][x]!=0:
                    d=[(y,x),(y-1,x),(y,x-1),(y-1,x-1)]
                    for location in d:
                        toRemove.add(location)

        if len(toRemove)==0:
            break
        else:
            count+=len(toRemove)

        for ry,rx in toRemove:
            board[ry][rx]=0

        for x in range(n - 1, -1, -1):
            for y in range(m - 1, 0, -1):
                if board[y][x]==0:
                    for ty in range(y-1,-1,-1):
                        print(ty,x)
                        if board[ty][x]!=0:
                            board[y][x]=board[ty][x]
                            board[ty][x]=0
                            break

    for row in board:
        print(row)
    print(count)
    return (count)


solution(5,6,["AAAAAA","BBAATB","BBAATB","JJJTAA","JJJTAA"])
# solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
# solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])