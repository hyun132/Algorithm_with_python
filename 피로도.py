def solution(k, dungeons):
    print(dfs(k, dungeons, []))


def dfs(tiredness, dungeons, visited):
    if visited == len(dungeons) - 1 or tiredness <= 0: return len(visited)
    count = len(visited)
    for i in range(len(dungeons)):
        if i not in visited:
            needed, cost = dungeons[i]
            if needed <= tiredness:
                count = max(count, dfs(tiredness - cost, dungeons, visited + [i]))
    return count


solution(80, [[80, 20], [50, 40], [30, 10]])
