import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

def countSafetyArea(board,walls,virus):
    temp = deepcopy(board)
    for y, x in walls:
        temp[y][x] = 1
    for y,x in virus:
            if temp[y][x] == 2:
                bfs(temp, y, x)
    sum =0
    for row in temp:
        sum += row.count(0)

    return sum


def bfs(tempboard, sy, sx):
    q = deque()
    q.append([sy, sx])
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < n and 0 <= nx < m and tempboard[ny][nx] == 0:
                tempboard[ny][nx] = 2
                if [ny,nx] not in q:
                    q.append([ny,nx])

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split(' '))
    board = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
    virus=[]
    empty = []
    for y in range(n):
        for x in range(m):
            if board[y][x] == 2:
                virus.append([y,x])
            if board[y][x] == 0:
                empty.append([y, x])

    cases = combinations(empty, 3)

    maxArea = 0
    for case in cases:
        maxArea = max(maxArea, countSafetyArea(board, case,virus))

    print(maxArea)


