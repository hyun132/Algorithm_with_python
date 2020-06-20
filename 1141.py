import re
import sys

n=int(sys.stdin.readline().strip())

arr = [sys.stdin.readline().strip() for _ in range(n)]

arr.sort(key=lambda x:len(x), reverse=True)

maxnum=n
result = [1 for _ in range(n)]
size=sum(result)
cnt=0
while True:
    cnt+=1
    result = [1 for _ in range(n)]
    for i in range(size):
        if result[i]==0:
            continue
        for j in range(size):
            # if result[j] == 0:
            #     continue
            if i==j:
                continue
            if arr[i] == arr[j]:
                result[j]=0
            elif len(arr[i])<len(arr[j]) and None!=re.match('^'+arr[i],arr[j]):
                result[i]=0
                break
            elif len(arr[i])>len(arr[j]) and None!=re.match('^'+arr[j],arr[i]):
                result[j]=0

    # print(result)
    maxnum=min(maxnum,sum(result))
    if cnt==n:
        break
    else:
        size=sum(result)
print(maxnum)
