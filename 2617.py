import sys

def fun(dict, start):
    global cnt

    visited[start]=True
    for nxt in dict[start]:
        if visited[nxt]==False:
            cnt += 1
            fun(dict,nxt)

inputs=list(map(int,sys.stdin.readline().split()))
heavy=[[] for _ in range(inputs[0]+1)]
light=[[] for _ in range(inputs[0]+1)]



for i in range(inputs[1]):
    num=list(map(int,sys.stdin.readline().split()))
    light[num[0]].append(num[1])
    heavy[num[1]].append(num[0])

# print(heavy)
# print(light)

result=[0]*(inputs[0]+1)
for i in range(1,inputs[0]+1):
    cnt=0
    visited = [False] * (inputs[0] + 1)
    fun(light,i)
    # print(cnt)
    result[i]=cnt

    cnt=0
    visited = [False] * (inputs[0] + 1)
    fun(heavy,i)
    # print(cnt)
    result[i]=max(result[i],cnt)
    # print(cnt[0])
    # print(result[i])

# print(result)
ret=0
for i in range(1,len(result)):
    if result[i]>(inputs[0]//2):
        ret+=1

print(ret)
