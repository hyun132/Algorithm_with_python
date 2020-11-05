zeros=0
ones=0
def solution(arr):

    def depression(arr,size,sy,sx):
        cur=arr[sy][sx]
        global zeros
        global ones

        for y in range(sy,sy+size):
            for x in range(sx,sx+size):
                if cur!= arr[y][x]:
                    depression(arr,size//2,sy,sx)
                    depression(arr, size // 2, sy+size // 2, sx)
                    depression(arr, size // 2, sy, sx+size // 2)
                    depression(arr, size // 2, sy+size // 2, sx+size // 2)
                    return

        if arr[sy][sx]==1:
            ones+=1
        elif arr[sy][sx]==0:
            zeros+=1

    depression(arr,len(arr),0,0)
    # print([zeros,ones])
    return [zeros,ones]



# solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])