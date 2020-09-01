def solution(n, arr1, arr2):
    board=[]
    for i in range(n):
        tempstr=""

        temp=int(arr1[i])|int(arr2[i])
        temp=bin(temp)
        zeros="0"*(n-len(temp[2:]))
        temp =  zeros+ temp[2:]

        for ch in temp:
            if ch=='1':
                tempstr+="#"
            else:
                tempstr+=" "

        board.append(tempstr)

    return board




solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])