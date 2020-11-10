import math
from itertools import combinations


def solution(nums):
    numSet=set(i for i in range(1,2998))
    count=0
    # numSet에는 소수만 남겨둔다
    for i in range(2,int(math.sqrt(2998))):
        temp=set()
        for num in list(numSet):
            if num%i==0 and num!=i:
                # print(num,i)
                temp.add(num)
        numSet=numSet-temp

    # 뽑은 세 수 합이 numSet에 있는지 확인한다
    for case in list(combinations(nums,3)):
        if sum(list(case)) in numSet:
            count+=1  # 소수이면 count 1

    return count

solution([1,2,7,6,4])