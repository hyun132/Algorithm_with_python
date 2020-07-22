import sys

N = int(sys.stdin.readline().strip())

arr=[1,2]+[0]*(N-2)

for i in range(2,N):
    arr[i]=(arr[i-2]+arr[i-1])%10007

print(arr[N-1])