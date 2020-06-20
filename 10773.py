import sys

case=int(sys.stdin.readline().strip())
stack=[]
for _ in range(case):
    input=int(sys.stdin.readline().strip())
    if input==0:
        if len(stack)==0:
            continue
        else:stack.pop()
    else:
        stack.append(input)

print(sum(stack))