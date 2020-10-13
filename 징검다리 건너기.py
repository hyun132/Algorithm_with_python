import sys


def solution(stones, k):

    if k==1:
        return min(stones)
    l=-1
    er=len(stones)
    answer=sys.maxsize
    while er-l>k:
        r=min(l+k,len(stones)-1)
        # print(l+1,r+1)
        temp=max(stones[l+1:r+1])
        answer=min(answer,temp)
        stone=stones[l+1:r+1]
        stone.reverse()
        l+=(k-stone.index(temp))

        el=max(er-k,-1)
        val=max(stones[el:er])
        answer=min(answer,val)
        stone=stones[el:er]
        er-=k-stone.index(val)


    return answer

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	,3)