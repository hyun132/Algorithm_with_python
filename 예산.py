import sys

def fun(m,budgets):
    val=0
    for item in budgets:
        if item > m:
            val += m
        else:
            val += item

    return val

def solution(budgets, M):

    resultArr=[]

    total=sum(budgets)
    if total<=M:
        print(total)
        return total

    remain=sys.maxsize
    avg = total // len(budgets)

    l=min(budgets)
    r=max(budgets)
    # mid = avg
    answer=0
    while l<=r:
        mid = (l + r) // 2

        result=fun(mid,budgets)

        if result>M:
            r=mid-1

        elif result <= M:
            l=mid+1
            answer=mid

        print(l, r, answer)

    # print(resultArr[0][1])

    return answer
    # return resultArr[0][1]


solution([120, 110, 140, 150],485)
# solution([1,2,3,4,5,6,7,8,9,10], 56)