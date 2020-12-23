import sys
from collections import deque

leftStack=[ch for ch in sys.stdin.readline().strip()]
rightStack=deque()
n=int(input())

for i in range(n):
    temp = sys.stdin.readline().strip()
    if temp[0] == 'P':
        leftStack.append(temp[2])
    elif temp[0] == 'D':
        if rightStack:
            leftStack.append(rightStack.popleft())
    elif temp[0]=='L':
        if leftStack:
            rightStack.insert(0,leftStack.pop())
    elif temp[0]=='B':
        if leftStack:
            leftStack.pop()

print(''.join(leftStack)+''.join(rightStack))