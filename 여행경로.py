from copy import deepcopy

answer=[]
def solution(tickets):

    flight=dict()

    for ticket in tickets:
        if ticket[0] in flight:
            flight[ticket[0]].append(ticket[1])
        else:
            flight[ticket[0]]=[ticket[1]]

    for key in flight:
        flight[key].sort()


    def dfs(d,visited,toVisit):
        global answer
        if len(visited)== len(tickets)+1:
            answer.append(visited)
            return
        elif visited[-1] not in toVisit or len(toVisit[visited[-1]])<1:
            return
        else:
            for des in toVisit[visited[-1]]:
                copiedTo = deepcopy(toVisit)
                copiedTo[visited[-1]].remove(des)
                dfs(d,visited+[des],copiedTo)

        return

    # copied=deepcopy(flight)
    dfs(0,["ICN"],flight)
    print(sorted(answer)[0])
    return(sorted(answer)[0])


solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])