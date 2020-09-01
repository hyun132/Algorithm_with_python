import math


def solution(brown, yellow):

    total=yellow+brown
    for m in range(3,int(math.sqrt(total))+2):
        # print(m)
        if total%m==0 and (2*(total/m)==total-yellow-(2*m)+4):

            return max(m,total//m),min(m,total//m)



    # answer = []
    # return answer

solution(10,2)