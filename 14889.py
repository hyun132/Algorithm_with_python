import sys
from itertools import combinations
n=input()
n=int(n)
board=[]
nums = [i for i in range(n)]
result =0
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

for row in combinations(nums,int(n/2)):
    team1 =list(row)
    team2 = list(set(nums) - set(team1))

    sum1=0
    sum2=0

    for x,y in list(combinations(team1,2)):
        sum1=sum1+(board[x][y]+board[y][x])

    for x,y in list(combinations(team2,2)):
        sum2=sum2+(board[x][y] + board[y][x])

    if result>abs(sum1-sum2):
        result = abs(sum1-sum2)

print(result)