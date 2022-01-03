import sys
from math import sqrt


# 접근방법1 배열에 가장 가까운 소수를 저장하고 입력값에서 현재 소수를 뺀 값이 소수인지 판별하여 값을 구한다.
def my_solutin_1():
    repeat = int(sys.stdin.readline().strip())

    # 먼저 소수를 구한다. decimal에는 가장 가까운 자신보다 작거나 같은 소수가 저장되어있다.
    decimal = [0, 1, 2] + [0] * 9997
    max_decimal = 2
    for num in range(1, 10000):
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                decimal[num] = max_decimal
                break
        if decimal[num] == 0:  # 만약 소수라면
            max_decimal = num
            decimal[num] = num

    for _ in range(repeat):
        n = int(sys.stdin.readline().strip())

        # n은 무조건 짝수
        for dec in range(n // 2, n):
            if decimal[n - decimal[dec]] == n - decimal[dec]:  # i와 가장 가까운 소수를 뺀 값이 소수인지 확인.
                print(min(decimal[dec], n - decimal[dec]), max(decimal[dec], n - decimal[dec]))
                break


def my_solution2():
    repeat = int(sys.stdin.readline().strip())
    is_decimal = [False, True, True] + [True, False] * 4999

    for i in range(2, 100):
        if is_decimal[i]:
            is_decimal[i * 2::i] = [False] * len(is_decimal[i * 2::i])

    for _ in range(repeat):
        n = int(sys.stdin.readline().strip())

        for num in range(n // 2, n):  # 순차적으로 숫자를 늘려가며 현재값과 입력값에서 현재값을 뺀 두 수 모두 소수인지 판별하여 값을 구한다.
            if is_decimal[num] and is_decimal[n - num]:
                print(n - num, num)
                break

# my_solutin_1()
# my_solutin_2()
