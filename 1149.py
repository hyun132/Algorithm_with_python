import sys
from collections import deque

# def fun(start):
#     visited= [[1000]*len(board[0]) for i in range(int(h))]
#     visited[0]=board[0]
#     need_visit=deque()
#     need_visit.append(start)
#
#     row={0:[1,2], 1:[1,2],2:[0,1]}
#     while need_visit:
#         node=need_visit.pop()
#         x,y=node
#         for i in row[y]:
#             if x+1<len(board):
#                 need_visit.append([x + 1, i])
#                 if visited[x+1][i] > visited[x][y]+board[x+1][i]:
#                     visited[x+1][i] = visited[x][y]+board[x+1][i]
#
#     sumarr.append(min(visited[-1]))


h = sys.stdin.readline()
sumarr=[]
board = []
for i in range(int(h)):
    board.append(list(map(int, sys.stdin.readline().split())))

dp=board

for i in range(1,int(h)):
    dp[i][0] = board[i][0]+min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = board[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = board[i][2] + min(dp[i - 1][1], dp[i - 1][0])

print(min(dp[int(h)-1]))