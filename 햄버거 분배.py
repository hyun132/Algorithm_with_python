import sys

N,K=map(int,sys.stdin.readline().split())

inputs=sys.stdin.readline().strip()

arr=[]

for ch in inputs:
    if ch == 'H':
        arr.append(False)
    else:
        arr.append(True)
# print(inputs)
# print(arr)

cnt=0
for i in range(len(inputs)):
    if inputs[i]=='H':
        for idx in range(max(i-K,0),min(i+K+1,len(inputs))):
            if arr[idx]==True:
                arr[idx]=False
                cnt+=1
                break


print(cnt)
