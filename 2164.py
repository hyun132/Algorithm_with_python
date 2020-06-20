import sys
from collections import deque

num=int(sys.stdin.readline().strip())
# num=int(num)

card=deque()
for i in range(int(num),0,-1):
    card.append(i)
# print(card)
while card:
    if len(card)==1:
        print(card.pop())
        break
    else:
        card.pop()
        card.insert(0,card.pop())
