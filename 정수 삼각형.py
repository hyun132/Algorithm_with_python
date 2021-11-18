def solution(triangle):
    for rowNumber in range(1,len(triangle)):
        for index in range(rowNumber + 1):
            print(rowNumber, index)
            if index == 0:
                triangle[rowNumber][0] += triangle[rowNumber - 1][0]
            elif index == rowNumber:
                triangle[index][index] += triangle[index - 1][index - 1]
            else:
                triangle[rowNumber][index] += max(triangle[rowNumber-1][index -1], triangle[rowNumber-1][index])
    return max(triangle[-1])


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
