def solution(n):
    route = dict()

    def hanoi(block, s, e):
        if block == 1:
            return [[s,e]]
        else:
            if (block, s, e) not in route.keys():
                via = 6-s-e
                route[(block, s, e)] = hanoi(block - 1, s, via) + [s,e] + hanoi(block - 1, via, e)
            return route[(block, s, e)]

    print(hanoi(n, 1, 3))

solution(2)
