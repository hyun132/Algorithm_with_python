N = int(input().strip())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:(x[1],x[0]))
finished=0
answer=0
for c in arr:
    if finished>c[0]:
        continue
    finished=c[1]
    answer+=1

print(answer)