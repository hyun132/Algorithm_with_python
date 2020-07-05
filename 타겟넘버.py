def dfs(size, target, d,sumval,numbers):
    if d==size:
        if sumval==target:
            global answer
            answer +=1
        return

    dfs(size,target,d+1,sumval+numbers[d],numbers)
    dfs(size, target, d + 1, sumval - numbers[d], numbers)

answer =0
def solution(numbers, target):
    size=len(numbers)
    dfs(size,target,0,0,numbers)
    print(answer)
    return answer

# solution([1, 1, 1, 1, 1],3)