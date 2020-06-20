import sys

board=[list(sys.stdin.readline().strip()) for _ in range(8)]
# print(board)
cnt=0
for y in range(8):
    for x in range(8):
        if (x+y)%2==0 and board[y][x]=='F':
            cnt+=1

print(cnt)