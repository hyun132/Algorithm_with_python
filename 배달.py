import sys
from collections import defaultdict, deque


def solution(N, road, K):
    dp = [sys.maxsize] * (N + 1)
    dp[1] = 0

    graph = defaultdict(list)

    for s, e, d in road:
        graph[s].append([e, d])
        graph[e].append([s, d])

    return bfs(graph, dp, K)


def bfs(graph, dp, K):
    q = deque([[1, 0]])

    while q:
        current, dist = q.popleft()
        for nextNode, nextDist in graph[current]:  # 현재 노드에서 연결된 다른 노드들
            if dp[current] + nextDist < dp[nextNode]:
                dp[nextNode] = dp[current] + nextDist
                if [nextNode, nextDist] not in q:
                    q.append([nextNode, nextDist])

    return len(list(filter(lambda x: x <= K, dp)))


solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
