import heapq
import sys
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size = int(input())
    board = [[int(ch) for ch in input().strip()] for _ in range(size)]
    visited = [[sys.maxsize] * size for _ in range(size)]

    start = [0, 0]
    visited[0][0]=0
    q = [[0, start]]
    answer = []
    flag = False
    while q:
        cost, c = heapq.heappop(q)
        cy, cx = c

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < size and 0 <= nx < size:
                if visited[cy][cx] + board[ny][nx] < visited[ny][nx]:
                    visited[ny][nx] = cost + board[ny][nx]
                    if [ny, nx] == [size - 1, size - 1]:
                        flag = True
                        break
                    if [ny, nx] not in q:
                        heapq.heappush(q, [visited[ny][nx], [ny, nx]])
        if flag:
            break

    print("#" + str(test_case) + " " + str(visited[size - 1][size - 1]))
