import sys
from collections import deque

def fun(start,k,max):
    cnt=[0]*(max+1)
    # visited=deque()
    # visited.append(start)
    q=deque()
    q.append(start)

    while q:
        # print(arr)
        n=q.popleft()
        if n==k:
            print(cnt[n])
            exit()
        d = (1, -1, n)
        for i in d:
            idx=n+i
            # print(idx)
            if 0<=idx<max:
                if cnt[idx]==0 or cnt[idx]>cnt[n]+1:
                    q.append(idx)
                    cnt[idx]=cnt[n]+1
                    # visited.append(idx)

n,k=list(map(int,sys.stdin.readline().split()))

if n>k:
    max=n
else:
    max=100001
if n==k:
    print(0)
else:
    fun(n,k,max)