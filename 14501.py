import sys

N = int(sys.stdin.readline().strip())

board=[[] for _ in range(N+1)]

for i in range(N):
    inputs=list(map(int,sys.stdin.readline().strip().split()))
    if inputs[0]+i>N:
        continue
    board[inputs[0]+i].append(inputs)

# print(board)
arr=[0]*(N+1)

for i in range(1,N+1):
    # print(i-board[i][0]+1)
    if board[i] == []:
        arr[i]=arr[i-1]
        continue
    val=arr[i-1]
    for temp in board[i]:
        # print(i, board[i], i - temp[0] + 1,arr[i-temp[0]+1]+temp[1])
        val = max(arr[i-temp[0]]+temp[1],val)
    arr[i] = val
# print(arr)
print(arr[-1])

