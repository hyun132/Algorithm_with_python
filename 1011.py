# import sys
# from math import sqrt
#
# repeat = int(sys.stdin.readline())
# for _ in range(repeat):
#     x, y = map(int, sys.stdin.readline().split(' '))
#     cumulative_sum = 0
#     gap = 1
#     for i in range(1, round(sqrt(y - x)) + 2):
#         if i * (i - 1) < y - x <= i * (i + 1):
#             answer = gap
#             if y - x > i * i: answer = answer + 1
#             break
#         else:
#             gap += 2
#
#     print(answer)

import sys

repeat = int(input())

for i in range(repeat):
    x, y = map(int, sys.stdin.readline().split())
    gap = y - x
    t = int(pow(gap - 1, 0.5))
    if t ** 2 < gap <= t ** 2 + t:
        print(t * 2)
    else:
        print(t * 2 + 1)
