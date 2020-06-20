import sys

arr=[]
for i in range(10):
    arr.append(int(sys.stdin.readline())%42)

arr=set(arr)
print(len(arr))