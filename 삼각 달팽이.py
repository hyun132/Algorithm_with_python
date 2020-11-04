def solution(n):

    d=[(1,0),(0,1),(-1,-1)]
    idx=0

    board=[[0]*n for _ in range(n)]

    y=-1
    x=0
    num=1
    for i in range(n-1,-1,-1):
        for _ in range(0,i+1):
            y=y+d[idx][0]
            x=x+d[idx][1]
            board[y][x]=num
            num+=1
        idx=(idx+1)%3

    answer=[]
    for r in range(n):
        temp=[one for one in board[r] if one!=0]
        answer.extend(temp)
        
    return answer

# solution(4)
solution(5)
