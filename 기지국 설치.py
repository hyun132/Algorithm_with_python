import math


def solution(n, stations, w):
    idx=0
    temp=0
    cnt=0
    s=1
    for e in stations:
        cnt+=math.ceil(((e-w)-s)/(2*w+1))
        s=e+w+1

    if s<=n:
        cnt+=math.ceil((n+1-s)/(2*w+1))

    print(cnt)
solution(11,[4,11],1)
# solution(16,[9],2)