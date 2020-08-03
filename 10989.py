import sys

N=int(sys.stdin.readline().strip())

arr=[0 for i in range(10000)]

for i in range(N):
    # idx=int(sys.stdin.readline().strip())
    arr[int(sys.stdin.readline().strip())-1]+=1
    # heapq.heappush(arr,int(sys.stdin.readline().strip()))
#
for i in range(10000):
    for j in range(arr[i]):
        print(i+1)
        # sys.stdout.write(str(i+1))
        # sys.stdout.write('\n')

