from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (N+1)
d, now = 0, [1]
visited[1] = 1
while 1:
    nxt = deque()
    for i in now:
        for j in arr[i]:
            if visited[j]:
                continue
            nxt.append(j)
            visited[j] = 1
    if nxt:
        now = nxt
        d += 1
    else:
        print(min(now), d, len(now))
        break