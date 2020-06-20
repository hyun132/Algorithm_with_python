import sys

case=int(sys.stdin.readline())
for i in range(case):
    n,m=list(map(int,sys.stdin.readline().split()))
    task=list(map(int, sys.stdin.readline().split()))
    if n==1:
        print(1)
        continue
    seq=[]
    for t in range(n):
        seq.append(t)
    # print(arr)
    count=0
    #
    # print(seq)
    # print(task)
    while True:
        maxnum=max(task)
        a=task.pop(0)
        temp=seq.pop(0)
        # print(a)
        if maxnum==a:
            if m == temp:
                print(n - len(task))
                task = []
                break
        if a < maxnum:
                task.append(a)
                seq.append(temp)



