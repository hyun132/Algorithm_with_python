import sys
#
#
def fun1(arr,m):
    # 먼저 시작
    sum=0
    for i in range(len(arr)-1,-1,-m):
        sum+=arr[i]*2
        # print(arr[i])
    # print(sum)
    return sum

n,m=list(map(int,sys.stdin.readline().split()))
#
arr=list(map(int,sys.stdin.readline().split()))
parr=[]
marr=[]
for i in arr:
    if i>0:
        parr.append(i)
    else:
        marr.append(-1*i)

parr.sort()
marr.sort()
# print(parr)
# print(marr)
# print(fun2(marr,m))
if len(parr)>0 and len(marr)>0:
    result=fun1(parr,m)+fun1(marr,m)
    result=result-max(parr[-1],marr[-1])
    print(result)
else:
    if len(parr)>0:
        print(fun1(parr, m)-parr[-1])
    elif len(marr)>0:
        print(fun1(marr, m)-marr[-1])
# b=fun2(parr,m)+fun1(marr,m)
# # print(min(a,b))
# #
#
# # def fun(start,sum,m):
# #     for i in range(start,start+m):
# #         if
# #         sum += arr[i] * 2
# #         fun(i,sum,m)
# # #         sum -= arr[i] * 2
# #
# # print(fun(0,0,2))