import sys

t= int(sys.stdin.readline().strip())

for _ in range(t):
    answer = "YES"
    n = int(sys.stdin.readline().strip())
    arr=[]

    for i in range(n):
        arr.append(sys.stdin.readline().strip())

    arr.sort()
    for w1,w2 in zip(arr,arr[1:]):
        if w2.startswith(w1):
            answer="NO"
            break
    print(answer)


    # print(answer)


    # arr.sort(key = lambda x:(x,len(x)))

    # print(answer)