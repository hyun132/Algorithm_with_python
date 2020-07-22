import sys

qSize,num=list(map(int,sys.stdin.readline().strip().split()))

nums= list(map(int,(sys.stdin.readline().strip().split())))
arr=[i for i in range(qSize)]
visited=[0 for _ in range(qSize+1)]

curNum=1
cnt=0
for target in nums:
    if curNum!=target:
        if curNum<target:
            cnt+=min(target-curNum-sum(visited[curNum+1:target]),curNum+qSize-target-sum(visited[:curNum]+visited[target+1:]))

        else:
            # curNum>target
            cnt+=min(curNum-target-sum(visited[target+1:curNum]),target+qSize-curNum-sum(visited[:target]+visited[curNum+1:]))
            # print(cnt)
    # print(curNum, target, cnt)
    visited[target] = 1
    i=0
    while i<qSize:
        if visited[(target+i) % qSize + 1]==0:
            curNum=(target+i) % qSize + 1
            break
        i+=1

# print()
print(cnt)