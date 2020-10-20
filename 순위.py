from collections import defaultdict


def solution(n, results):

    winner=defaultdict(set) #key 가 이긴사람들
    loser=defaultdict(set)  # key한테 진사람들

    for w,l in results:
        winner[w].add(l)
        loser[l].add(w)

    for i in range(1,n+1):
        for w in loser[i]:  # i를 이긴 애들이
            winner[w].update(winner[i])  # i가 이긴 애들 포함

        for l in winner[i]:
            loser[l].update(loser[i])


    count=0
    for i in range(1,n+1):
        if winner[i]+loser[i]==n-1:
            count+=1

    return count



solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
# solution(4,[[1,2],[1,3],[2,4]])
