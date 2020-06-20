import sys
from collections import deque

case=int(sys.stdin.readline().strip())
a=deque()
b=deque()
for _ in range(case):
    str=sys.stdin.readline().strip()
    pw=""
    idx=0
    for ch in str:
        if ch=="<":
            if a:
                b.appendleft(a.pop())
        elif ch==">":
            if b:
                a.append(b.popleft())
        elif ch =='-':
            if a:
                a.pop()
        else:
            a.append(ch)

    print("".join(a)+"".join(b))
    a.clear()
    b.clear()