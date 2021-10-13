from collections import defaultdict

BRUSH = 100


def solution(enroll, referral, seller, amount):
    # key의 value가 본인의 부모
    parent = defaultdict(str)
    income = defaultdict(int)

    for child, parents in zip(enroll, referral):
        parent[child] = parents

    for who, selled in zip(seller, amount):
        money = selled * BRUSH
        child = who
        parents = parent[child]
        income[child] += money

        while money > 0 and parents!='-':
            income[parents] += money // 10
            income[child] -= money // 10
            money //= 10
            child = parent[child]
            parents = parent[parents]

        income[child] -= money // 10

    return [income[who] for who in enroll]



#
# solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
#          ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"],
#          [12, 4, 2, 5, 10])
solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"],
         [2, 3, 5, 4])
