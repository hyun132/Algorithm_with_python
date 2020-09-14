def solution(nums):
    pick=len(nums)/2

    poketmon=set(nums)

    if len(poketmon)<=pick:
        return len(poketmon)
    else:
        return pick


solution([3,1,2,3])