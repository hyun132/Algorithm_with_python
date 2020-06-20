import sys

board=[[''] for _ in range(5)]
max=0
for i in range(5):
    str=sys.stdin.readline().strip()
    for item in str:
        board[i].append(item)
    if len(board[i])>max:
        max=len(board[i])


for x in range(max):
    for y in range(5):
        if len(board[y])>x:
            if board[y][x]!='':
                print(board[y][x],end='')