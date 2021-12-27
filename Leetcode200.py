from collections import deque


# 얘가 성능 더 좋음 260 ms
def numIslands_bfs(grid) -> int:
    count = 0

    def bfs(start):
        q = deque([start])
        grid[start[0]][start[1]] = "0"  # y,x

        while q:
            y, x = q.popleft()

            if y + 1 < len(grid) and grid[y + 1][x] == "1":
                q.append([y + 1, x])
                grid[y + 1][x] = "0"

            if y > 0 and grid[y - 1][x] == "1":
                q.append([y - 1, x])
                grid[y - 1][x] = "0"

            if x + 1 < len(grid[0]) and grid[y][x + 1] == "1":
                q.append([y, x + 1])
                grid[y][x + 1] = "0"

            if x > 0 and grid[y][x - 1] == "1":
                q.append([y, x - 1])
                grid[y][x - 1] = "0"

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "1":
                bfs([y, x])
                count += 1
    return count


# 308 ms
def numIslands_dfs(grid) -> int:
    def dfs(y, x):
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] == "0":
            return

        grid[y][x] = "0"
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x - 1)
        dfs(y, x + 1)

    count = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "1":
                count += 1
                dfs(y, x)

    return count
