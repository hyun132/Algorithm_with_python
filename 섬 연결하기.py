def solution(n, costs):

    costs.sort(key= lambda x:x[2])
    totalCost=costs[0][2]
    graph=set()
    graph.add(costs[0][0])
    graph.add(costs[0][1])
    while True:
        for cost in costs:
            if cost[0] in graph and cost[1] in graph:
                continue
            if cost[0] in graph and cost[1] not in graph:
                graph.add(cost[1])
                totalCost += cost[2]
                break
            elif cost[1] in graph and cost[0] not in graph:
                graph.add(cost[0])
                totalCost+=cost[2]
                break
        if len(graph)==n:
            print(totalCost)
            break
        print(graph)
    print(totalCost)


# solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
solution(5, [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]])
# solution(5,[[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]])
# solution(5, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]] )
# solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])
# solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]])
# solution(5,[[0,1,1],[3,4,1],[1,2,2],[2,3,4]])