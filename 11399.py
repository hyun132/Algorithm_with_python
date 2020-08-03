import sys
import heapq

N = int(sys.stdin.readline().strip())
arr=list(map(int,sys.stdin.readline().split()))


total=0
waiting=0
arr.sort()
for time in arr:
    waiting+=time
    total+=waiting

print(total)

