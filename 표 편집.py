# 답은 나오지만 효율성이 어림도 없음..ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
def solution(n, k, cmd):
    current = [i for i in range(n)]
    stack = []

    for operator in cmd:
        op = operator[0]
        if op == "D":
            k += int("".join(operator[2:]))
        elif op == "U":
            k -= int("".join(operator[2:]))
        elif op == "C":
            stack.append([k, current[k]])
            current.remove(current[k])
            if k == len(current): k -= 1
        elif op == "Z":
            if (stack):
                idx, staticIdx = stack.pop()
                current.insert(idx, staticIdx)
                if idx <= k: k += 1

    result = ["X"] * n
    for i in current:
        result[i] = "O"
    # print("".join(result))
    return "".join(result)


# 많은 다른 풀이가 있지만 가장 이상적이라고 생각한 건 링크드 리스트를 사용하는것. 그리고 노드는 딕셔너리를 이용한다.
def solution2(n, k, cmd):
    nodes = dict()

    stack = []
    for i in range(n):
        if i == 0:
            nodes[i] = [0, i + 1]
        elif i == n - 1:
            nodes[i] = [i - 1, i]
        else:
            nodes[i] = [i - 1, i + 1]

    for operator in cmd:
        op = operator[0]
        if op == "D":
            for _ in range(int("".join(operator[2:]))):
                k = nodes[k][1]
        elif op == "U":
            for _ in range(int("".join(operator[2:]))):
                k = nodes[k][0]
        elif op == "C":
            stack.append([k, nodes[k]])
            if nodes[k][1] == k:
                nodes[nodes[k][0]][1] = nodes[k][0]
                k = nodes[k][0]
            elif nodes[k][0] == k:
                nodes[nodes[k][1]][0] = nodes[k][1]
                k = nodes[k][1]
            else:
                nodes[nodes[k][0]][1] = nodes[k][1]
                nodes[nodes[k][1]][0] = nodes[k][0]
                k = nodes[k][1]

        elif op == "Z":
            if (stack):
                idx, node = stack.pop()
                if idx != node[1]:
                    nodes[node[1]][0] = idx
                if idx != node[0]:
                    nodes[node[0]][1] = idx

    answer = ["O"] * n
    for idx in [node[0] for node in stack]:
        answer[idx] = "X"

    return "".join(answer)


solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])  # "OOOOXOOO"
solution2(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])  # "OOXOXOOO"
