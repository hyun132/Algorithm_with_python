import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        for node in times:
            graph[node[0]].append((node[2], node[1]))

        print(graph)
        next_list = [(0, k)]
        answer = 0

        while len(next_list) > 0:
            cur = heapq.heappop(next_list)
            print(cur)
            if cur[1] not in visited:
                visited.add(cur[1])
                answer = max(answer, cur[0])
                for nxt in graph[cur[1]]:
                    heapq.heappush(next_list,(cur[0] + nxt[0], nxt[1]))

        if len(visited) == n:
            return answer
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    # print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    # print(sol.networkDelayTime([[1,2,1]], 2, 1))
    # print(sol.networkDelayTime([[1, 2, 1]], 2, 2))
    print(sol.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1))
    # print(sol.networkDelayTime(
    #     [[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]], 4, 1))
