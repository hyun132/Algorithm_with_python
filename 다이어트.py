import sys


def dfs(s,visited, nutrient, cost):

    for idx in range(4):
        if nutrient[idx]<limit[idx]:
            break
        if idx==3:
            arr.append([cost,visited])

    for i in range(s,N):
        if len(arr)>0:
            if min(arr)[0] <= cost:
                continue
        dfs(i+1, visited+[i+1],[ingredient[i][k] + nutrient[k] for k in range(4)], cost + ingredient[i][-1])

N = int(sys.stdin.readline().strip())

limit = list(map(int,sys.stdin.readline().strip().split()))

ingredient =[]
temparr=[0,0,0,0]
for i in range(N):
    ingredient.append(list(map(int, sys.stdin.readline().strip().split())))

arr=[]
dfs(0,[],[0 for _ in range(4)],0)
# print(arr)
if len(arr)>0:
    print(min(arr)[0])
    for i in min(arr)[1]:
        print(i,end=' ')
else:
    print(-1)


