# import sys
# #
# # size=int(sys.stdin.readline().strip())
# #
# # arr=list(map(int,sys.stdin.readline().split()))
# #
# # visited=[0 for _ in range(size)]
# #
# # result=[]
# # i=0
# # for l in range(size-1):
# #     i=l
# #     for j in range(i,size):
# #         print(i,j,visited)
# #         if arr[i]<arr[j]:
# #             if visited[j]<visited[i]+1:
# #                visited[j]=visited[i]+1
# #                i=j
# #     print(i, j, visited)
# # print(visited[-1]+1)
import sys

size=int(sys.stdin.readline().strip())

arr=list(map(int,sys.stdin.readline().split()))
dp = [0 for i in range(size)]
for i in range(size):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    # print(dp)
print(max(dp))
