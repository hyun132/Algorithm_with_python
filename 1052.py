# import sys
#
# # def fun(s,e):
# #     if s==e:
# #         return
# cnt=0
#
# n,k=map(int,sys.stdin.readline().strip().split())

# arr=[1 for _ in range(n)]
# if n%2!=0:
#     arr.append(1)
#     cnt+=1
#
# s=0
# e=len(arr)-1
# while True:
#     flag=0
#     while True:
#         if arr[s]==arr[e]:
#             arr[s]*=2
#             arr.pop(e)
#             e-=1
#             s+=1
#             flag=1
#         else:
#             e-=1
#         if s>=e:
#             break
#     # print(arr,s,e)
#     if len(arr)<=k:
#         break
#     if flag==0:
#         s +=1
#         if s!=0 and s==len(arr)-1:
#             cnt+=arr[-1]
#             arr.append(arr[-1])
#             s=0
#     else:
#         s=0
#     e = len(arr) - 1
#
#     # print(arr, s, e)
# print(cnt)

import sys
from collections import Counter

# cnt=0
#
# def fun(n):
#     cnt=0
#     # strnum= format(n,'b')
#
#     # print(strnum)
#     # print(n)
#     # print(bin(n))
#     for i in range(len(bin(n))-2):
#         # print(n&1<<i)
#         if n&1<<i!=0:
#             cnt+=1
#     return cnt
# n,k=map(int,sys.stdin.readline().strip().split())



# sum=0
# arr=[0 for _ in range(7)]
# print(bin(n))

# temp=n
# while True:
#     num_of_one=0
#     for i in range(len(bin(temp))-2):
#         # print(n&1<<i)
#         if temp&1<<i!=0:
#             num_of_one+=1
#
#     if num_of_one>k:
#         temp+=1
#     elif num_of_one<=k:
#         print(temp-n)
#         break
# # print(cnt)

n,k=map(int,input().split())
c=0
while bin(n).count('1')>k:
 #    맨뒷자리 1
 a=2**(bin(n)[::-1].index('1'))
 c+=a
 n+=a
 print(n,c,a)
print(c)