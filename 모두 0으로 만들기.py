from collections import defaultdict
import sys
# python에서 재귀 default limit 값 늘려주어야 돌아감
sys.setrecursionlimit(300000)


def solution(a, edges):
    global answer

    if sum(a) != 0: return -1
    valueArr = a
    graph = defaultdict(list)
    answer = 0

    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    dfs(0, graph, valueArr)

    return answer


def dfs(start, graph, valueArr):
    tempSum = valueArr[start]
    global answer
    valueArr[start] = 0
    for node in graph[start]:
        if valueArr[node] == 0: continue
        tempSum += dfs(node, graph, valueArr)

    answer += abs(tempSum)
    return tempSum

solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]])
# solution([0, 1, 0], [[0, 1], [1, 2]])
