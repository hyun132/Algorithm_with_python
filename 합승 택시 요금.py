import heapq
# from collections import defaultdict, deque
import sys

## Floyd Warshall
def solution(n, s, a, b, fares):
    s,a,b=s-1,a-1,b-1
    MAX_SIZE = sys.maxsize
    board = [[MAX_SIZE]*(n) for _ in range(n)]

    for n1,n2,d in fares:
        n1,n2 = n1-1, n2-1
        board[n1][n2] = board[n2][n1] = d
        board[n1][n1]=0
        board[n2][n2]=0

    for ss in range(n):
        for mm in range(n):
            for ee in range(n):
                if board[mm][ee] > board[mm][ss]+board[ss][ee]:
                    board[mm][ee] = board[mm][ss]+board[ss][ee]

    totalCost = board[s][a]+board[s][b]

    for i in range(n):
        totalCost = min(totalCost, board[s][i]+board[i][a]+board[i][b])

    for r in board:
        print(r)

    print(totalCost)


## dijkstra

# def solution(n, start, a, b, fares):
#     map = defaultdict(list)
#
#     for s, e, d in fares:
#         map[s].append([d, e])
#         map[e].append([d, s])
#
#     cost = sys.maxsize
#     for i in range(n + 1):
#         cost = min(cost , dijkstra(start, i, map) + dijkstra(i, a, map) + dijkstra(i, b, map))
#     return cost
#
#
# def dijkstra(s, e, map):
#     n = max(map.keys())
#     q = [[0,s]]
#     costArr = [sys.maxsize] * (n+1)
#     costArr[s]=0
#
#     while q:
#         cost, dest = heapq.heappop(q)
#
#         for item in map[dest]:
#             nc, nd = item
#             if costArr[dest] + nc < costArr[nd]:
#                 costArr[nd] = costArr[dest] + nc
#                 if [nc,nd] not in q:
#                     heapq.heappush(q, [costArr[nd], nd])
#
#         if dest == e:
#             break
#     return costArr[e]


solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
# solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
# solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])