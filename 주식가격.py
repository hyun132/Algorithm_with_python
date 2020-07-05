from collections import deque


def solution(prices):
    stack=deque()
    size=len(prices)
    answer = [0]*size
    for i in range(size):
        if len(stack)==0 or prices[i]>stack[-1][0]:
            stack.append((prices[i],i))
        else:
            while True:
                if len(stack)>0 and prices[i]<stack[-1][0]:
                    temp=stack.pop()
                    answer[temp[1]]=i-temp[1]
                else:
                    stack.append((prices[i], i))
                    break
        print(prices[i],stack)
    for item in stack:
        answer[item[1]]=size-1-item[1]
    print(answer)
    return answer

solution([1, 2, 3, 2, 3,3,3,3,2])#,[4, 3, 1, 1, 0]
# solution([1000,20])