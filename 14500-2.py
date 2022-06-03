# 두번째 풀이
import sys


def is_correct_position(y, x, visited):
    return 0 <= y < N and 0 <= x < M and [y, x] not in visited


def dfs(visited, position, sum_value):
    global answer

    # 4번째 블록까지 방문한 경우
    if len(visited) >= 4:
        answer = max(answer, sum_value)
        return

    # 보드 내의 최댓값을 더해줘도 max 현재 최댓값보다 작은 경우 가지치기
    if answer > (4 - len(visited)) * max_value + sum_value: return

    for dy, dx in d:
        y, x = dy + position[0], dx + position[1]
        if is_correct_position(y, x, visited):
            dfs(visited + [[y, x]], [y, x], sum_value + board[y][x])

            if len(visited) == 2:
                dfs(visited + [[y, x]], position,
                    sum_value + board[y][x])  # 예외케이스(ㅏ,ㅓ,ㅗ,ㅜ)를 위해 현재위치 갱신x


N, M = map(int, sys.stdin.readline().split(' '))

board = [(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]

max_value = 0
for row in board:
    max_value = max(max_value,max(row))

answer = 0
d = [(0, 1), (0, -1), (1, 0)]  # 위로 이동하는 경우는 이미 이전 케이스에서 확인했음. 최적화
for n in range(N):
    for m in range(M):
        dfs([[n, m]], [n, m], board[n][m])

print(answer)
