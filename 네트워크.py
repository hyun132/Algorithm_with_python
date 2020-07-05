from collections import Counter, deque

def bfs(visited,computers,n):

    for i in range(n):
        q = deque()
        network = set()
        if visited[i] != i:
            continue
        q.append(i)
        network.add(i)
        while q:
            s=q.popleft()
            for e in range(n):
                if computers[s][e]==1:
                    if e == visited[e] and e not in network:
                        q.append(e)
                        network.add(e)

        val=min(network)
        for item in network:
            visited[item]=val

def solution(n, computers):
    result=dict()

    visited=[i for i in range(n)]
    bfs(visited,computers,n,result)

    answer=Counter(visited)

    return len(answer)

solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
# solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])