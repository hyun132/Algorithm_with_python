# # 제일 처음에 풀었던 방식
# def solution1(word):
#     cases = []
#     dfs("", cases)
#     answer = sorted(cases).index(word) + 1
#     print(answer)
#     return answer
#
#
# def dfs(visited, cases):
#     if len(visited) == 5: return
#
#     for ch in ["A", "E", "I", "O", "U"]:
#         cases.append(visited + ch)
#         dfs(visited + ch, cases)


#라이브러리를 사용한 방식
from itertools import product

def solution2(word):
    arr = ["A", "E", "I", "O", "U"]
    answer = []
    for i in range(1, 6):
        for case in product(arr, repeat=i):
            answer.append("".join(case))

    return sorted(answer).index(word) + 1


solution2("AAAAE")  # 6
