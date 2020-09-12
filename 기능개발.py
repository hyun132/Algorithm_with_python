import math


def solution(progresses, speeds):

    idx=0
    answer=[]
    finished = 0

    num = math.ceil((100 - progresses[idx]) / speeds[idx])
    while True:
        if progresses[idx]+speeds[idx]*num<100:
            print(idx, finished)
            answer.append(finished)
            num = math.ceil((100 - progresses[idx]) / speeds[idx])
            finished = 0
        else:
            idx+=1
            finished+=1

        if idx>=len(progresses):
            # print(idx, finished)
            answer.append(finished)
            break

    print(answer)


solution([93, 30, 55],[1, 30, 5])
# solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])

# from math import ceil
# def solution(progresses, speeds):
#
#     days=[]
#     for i in range(len(progresses)):
#         days.append(ceil((100-progresses[i])/speeds[i]))
#     days.append(101)
#     # print(days)
#     answer = []
#     idx=0
#     for i in range(idx,len(days)):
#         if days[idx]<days[i] or idx==len(days)-1:
#             answer.append(i-idx)
#             idx=i
#     # print(answer)
#     return answer