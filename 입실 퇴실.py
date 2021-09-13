def solution(enter, leave):
    answer = [0] * len(enter)
    stack = []
    leaveIdx = 0
    for num in enter:
        # leaveIdx이 가리키는 값이 이미 스택에 있는지 확인하고 있으면 다 pop한다
        while leave[leaveIdx] in stack:
            stack.remove(leave[leaveIdx])
            leaveIdx += 1

        # 새로운 num값이 시작되면 일단 answer의 그 인덱스값을 스택길이로 만든다.
        answer[num-1] = len(stack)

        # 그리고 나머지 stack에 있는 애들 answer값 +1씩 해준다.
        for personNumber in stack:
            answer[personNumber-1]+=1

        # r이 가리키는 값이 stack에 있는지 확인하고 없으면 stack에 저장.
        stack.append(num)
    return answer


# solution([1, 3, 2], [1, 2, 3])
solution([1, 4, 2, 3], [2, 1, 3, 4])
