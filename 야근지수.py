import heapq


def solution(n, works):


    for i in range(len(works)):
        works[i]*=-1

    heapq.heapify(works)
    for i in range(n):

        item=heapq.heappop(works)
        if item>=0:
            break
        item+=1
        heapq.heappush(works,item)


    answer=0
    for item in works:
        answer+=pow(item,2)

    return answer





# solution(4,[4,3,3])
solution(3,[1,1])