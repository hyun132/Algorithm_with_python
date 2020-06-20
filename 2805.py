# # import sys
# #
# # n,m=map(int,sys.stdin.readline().split())
# #
# #
# # arr=list(map(int,sys.stdin.readline().split()))
# # # lenarr=[0 for _ in range(max(arr)+1)]
# # # print(len(lenarr))
# # arr.sort(reverse=True)
# # # print(arr)
# # # nums=dict()
# # # i=1
# # # for h in arr:
# # #     if h in nums:
# # #         nums[h]+=1
# # #     else:
# # #         nums[h]=i
# # #     i+=1
# # # # print(nums)
# # # sum=0
# # # num_of_trees=0
# # # for i in range(arr[0],-1,-1):
# # #     if i in nums.keys():
# # #         num_of_trees=nums[i]
# # #     sum += num_of_trees
# # #     if sum>=m:
# # #         print(i-1)
# # #         break
# # sum=0
# # num_of_trees=1
# # for i in range(1,len(arr)):
# #     if sum+num_of_trees*(arr[i-1]-arr[i])==m:
# #         print(i-1)
# #     elif arr[i-1] == arr[i]:
# #         num_of_trees+=1
# #     else:
# #         sum=sum + num_of_trees * (arr[i-1] - arr[i])
# #         num_of_trees += 1
# #
# # print(0)
#
# import sys
#
# n,m=map(int,sys.stdin.readline().split())
#
#
# arr=list(map(int,sys.stdin.readline().split()))
# arr.sort(reverse=True)
# lenarr=[0 for _ in range(max(arr)+1)]
# # print(len(lenarr))
# print(arr)
# size=len(arr)
# for i in range(max(arr),0,-1):
#     for h in arr:
#         lenarr[i]=size-len(arr)+1
#     if arr[-1]==i:
#         arr.pop()
# for i in range(len(lenarr)-2,0,-1):
#     lenarr[i]+=lenarr[i+1]
#
# print(lenarr)
#
# # print(lenarr)
#
# sum=0
# # for i in range(len(lenarr)-1,-1,-1):
# #     sum+=lenarr[i]
# #     if sum>=m:
# #         print(i-1)
# #         break
#
# s=0
# e=len(lenarr)-1
# while True:
#
#     # arr[s]=-1
#     # arr
#     mid=(s+e)//2
#     # print(s,e,mid)
#     if lenarr[mid]==m or lenarr[mid+1]>m>lenarr[mid-1]:
#         print(mid-1)
#         break
#
#     if lenarr[mid]>m:
#         s= mid + 1
#
#         # if arr[mid]==-1:
#         #     print(mid)
#         #     break
#     elif lenarr[mid]<m:
#         e = mid - 1
#
#
import sys

n,m=map(int,sys.stdin.readline().split())


arr=list(map(int,sys.stdin.readline().split()))

s=1
e=max(arr)

while True:
    sum = 0
    if s>e:
        print(e)
        break

    mid = (s+e)//2

    for i in arr:
        if i>=mid:
            sum+=(i-mid)
    if sum>=m:
        s = mid + 1

    else:
        e = mid - 1
# lenarr=[0 for _ in range(max(arr)+1)]
# print(len(lenarr))
# for h in arr:
#     for i in range(1,h+1):
#         lenarr[i]+=1

# print(lenarr)

# sum=0
# for i in range(len(lenarr)-1,-1,-1):
#     sum+=lenarr[i]
#     if sum>=m:
#         print(i-1)
#         break