def solution(arr):

    maxNum=max(arr)

    std=maxNum
    while True:
        flag=False
        for num in arr:
            if std%num!=0:
                flag=True
                break
        if flag==False:
            break
        std += maxNum

    return std


# solution([2,6,8,14])
solution([1,2,3])