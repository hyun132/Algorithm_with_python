import re
import sys
from itertools import combinations


def func1(): # 처음에 알고리즘이 생각나지 않아서 정규식으로 풀었으나 시간초과
    first_string = sys.stdin.readline().strip()
    second_string = sys.stdin.readline().strip()

    for i in range(len(second_string) - 1, 0, -1):
        for case in set(combinations(second_string, i)):
            if re.findall('[A-Z]*' + '[A-Z]*'.join(case) + '[A-Z]*', first_string):
                print(len(case))
                exit()


def func2(): #lcs 알고리즘 다시 찾아보고 푼 방법
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    lcs = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]

    for b_index in range(1, len(b) + 1):
        for a_index in range(1, len(a) + 1):
            if a[a_index - 1] == b[b_index - 1]:
                lcs[b_index][a_index] = lcs[b_index - 1][a_index - 1] + 1
            else:
                lcs[b_index][a_index] = max(lcs[b_index - 1][a_index], lcs[b_index][a_index - 1])

    print(lcs[len(b)][len(a)])


def func3(): # 2차원배열을 사용하지 않고 a[j]까지의 최댓값을 변수에 저장,비교하게 해서 시간을 단축하는 방법
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    dp = [0] * len(a)

    for i in range(len(b)):
        max_value = 0
        for j in range(len(a)):
            if dp[j] > max_value: max_value = dp[j]
            elif a[j] == b[i]: dp[j] = max_value + 1

    print(max(dp))