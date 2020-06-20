import sys
from collections import deque

arr=sys.stdin.readline().strip()
q=deque()
# cycle=len(arr)
sum=0
i=0
while i<len(arr):

    if arr[i]==')':
        if q[-1]=='(':
            if arr[i - 1] == '(':
                q.pop()
                sum+=q.count('(')
            else:
                q.pop()
                sum+=1
    else:
        q.append('(')
    # print(sum,q,arr[i])
    i+=1

print(sum)
