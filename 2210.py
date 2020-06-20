import sys
from collections import Counter, deque


def fun(case,start,result):
    sy,sx=start
    if len(case)==6:
        # print(case)
        result.add(case)
        return
    else:
        nd = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dy,dx in nd:
            y,x=dy+sy,dx+sx
            if 0<=y<5 and 0<=x<5:
                # if board[y][x] not in case:
                fun(case+board[y][x],(y,x),result)

board=[]
for _ in range(5):
    board.append(list(sys.stdin.readline().split()))

result = set()
for y in range(5):
    for x in range(5):
        fun(board[y][x],(y,x),result)
# print(result)
print(len(result))

