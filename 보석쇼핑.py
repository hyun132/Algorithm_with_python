from collections import defaultdict


def solution(gems):
    s, e = 0, 0
    min_length = len(gems)
    size = len(set(gems))
    cart = defaultdict(int)
    answer = [1, len(gems)]

    while e < len(gems):
        cart[gems[e]] += 1
        if len(cart) == size:  # 현재 구간에 모든 보석종루가 포함되어있으면
            while s <= e:  # 맨 앞부터 구간을 줄여가며 모든 보석을 가진 가장 작은 구간을 구한다.
                if cart[gems[s]] > 1:
                    cart[gems[s]] -= 1
                    s += 1
                else:
                    if min_length > e - s:
                        min_length = e - s
                        answer = [s + 1, e+1]
                    cart.pop(gems[s])
                    s += 1
                    break
        e += 1
    print(answer)

# solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
# solution(["AA", "AB", "AC", "AA", "AC"])
# solution(["XYZ", "XYZ", "XYZ"])
# solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
# solution(["A", "B" ,"B", "C", "A", "B", "C", "A","B","C"])
# solution(["DIA", "EM", "EM", "RUB", "DIA"])
solution([1, 1, 1, 1, 1, 1])


