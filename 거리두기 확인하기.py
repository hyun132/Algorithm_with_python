def solution(places):
    return [isSafe(case) for case in places]


def isSafe(case):
    for y in range(5):
        for x in range(5):
            if case[y][x] != "P": continue
            # 바로 인접한곳에 사람이 있을경우
            if (y < 4 and case[y + 1][x] == "P") or (x < 4 and case[y][x + 1] == "P"):
                return 0
            if y < 4 and x < 4 and case[y + 1][x + 1] == "P" and (case[y + 1][x] != "X" or case[y][x + 1] != "X"):
                return 0
            if y > 0 and x < 4 and case[y - 1][x + 1] == "P" and (case[y - 1][x] != "X" or case[y][x + 1] != "X"):
                return 0
            if y < 3 and case[y + 2][x] == "P" and "X" != case[y + 1][x]:
                return 0
            if x < 3 and case[y][x + 2] == "P" and "X" != case[y][x + 1]:
                return 0
    return 1

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
