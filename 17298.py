import sys

size = int(sys.stdin.readline().strip())
num_arr = list(map(int, sys.stdin.readline().strip().split(' ')))

stack = []
answer = [-1] * size

for index in range(size - 1, -1, -1):
    while stack:
        if stack[-1] <= num_arr[index]:
            stack.pop()
        else:
            break
    if stack:   #if stack and stack[-1] > num_arr[index]: 일 때는 왜 틀리는거야..
        answer[index] = stack[-1]
    stack.append(num_arr[index])
print(*answer)
