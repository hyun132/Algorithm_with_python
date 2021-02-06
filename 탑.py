n = int(input())
arr = list(map(int, input().split(' ')))
Stack = []

#현재것보다 이전탑이 높으면 이전거 출력
#이전찹이 낮으면 현재것보다 높은것 찾을때까지 pop
#만약 못찾고 stack이 비었으면 0 출력

for i in range(n):
    while Stack:
        if Stack[-1][1] > arr[i]:
            print(Stack[-1][0] + 1,end=" ")
            break
        Stack.pop()

    if not Stack:
        print(0,end=" ")

    Stack.append([i, arr[i]])
