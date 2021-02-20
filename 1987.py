#시간복잡도 조건이 까다로움.
import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

maxval=1

# 방문했던 노드인지 확인하는 조건 대신 set으로 걸러냄.
q = set([(0, 0, board[0][0])])
while q:
    y,x, visited = q.pop()
    maxval = max(maxval, len(visited))
    if maxval==26:
        break
    if 0 <= y + 1 < R and (board[y + 1][x] not in visited):
        q.add((y + 1, x, visited + board[y + 1][x]))

    if 0 <= y - 1 < R and (board[y - 1][x] not in visited):
        q.add((y - 1, x, visited + board[y - 1][x]))

    if 0 <= x + 1 < C and (board[y][x + 1] not in visited):
        q.add((y, x + 1, visited + board[y][x + 1]))

    if 0 <= x - 1 < C and (board[y][x - 1] not in visited):
        q.add((y, x - 1, visited + board[y][x - 1]))


print(maxval)
