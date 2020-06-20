import sys


def fun():

    N,M,V = map(int,sys.stdin.readline().split())
    graph=dict()
    graph2=dict()
    arr=[]
    for i in range(M):
        arr.append(list(map(int,sys.stdin.readline().split())))
    for i in range(1,N+1):
        n_arr=[]
        for item in arr:
            if i in item:
                if i==item[0]:
                    n_arr.append(item[1])
                else:
                    n_arr.append(item[0])
        n_arr.sort()
        graph2[i]=n_arr
        graph[i] = reversed(n_arr)
    for i in dfs(graph, V):
        print(i,end=' ')
    print()
    for i in bfs(graph2, V):
        print(i, end=' ')


def dfs(graph,start_node):
    visited,need_visit=list(),list()
    need_visit.append(start_node)

    while need_visit:
        node=need_visit.pop()
        if node not in visited:
            need_visit.extend(graph[node])
            visited.append(node)

    return visited

def bfs(graph,start_node):
    visited, need_visit=list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            need_visit.extend(graph[node])
            visited.append(node)
    return visited

fun()