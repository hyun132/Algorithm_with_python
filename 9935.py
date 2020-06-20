import re
import sys

string = sys.stdin.readline().strip()
target=sys.stdin.readline().strip()
# re.findall(target,string)
stack=[]
size=len(target)
for ch in string:

    stack.append(ch)

    if len(stack)>=size and "".join(stack[-size:]) == target:
        # print(stack[-size:])
        for _ in range(size):
            stack.pop()

if len(stack)==0:
    print("FRULA")
else:
    print("".join(stack))
# string=re.sub(target,"",string)
# print(string)
# while True:
#     tempstr=string
#     # string=string.replace(target,'')
#     string = re.sub(target, "", string)
#     if tempstr != string:
#         continue
#     break
# p=re.sub(target,string)
# re.compile(string,p)
# if string=="":
#     print("FRULA")
# else:
#     print(string)
# idx=0
# while True:
#     idx=string.find(target,idx)
#     if idx==-1:
#         break
#     # print(string[:idx]+string[idx+len(target)])
#     string=string[:idx]+string[idx+len(target):]
#     if idx-len(target)-1<0:
#         idx=0
#     else:
#         idx=idx - len(target)-1
#     # print(string)
# if len(string)==0:
#     print("FRULA")
# else:
#     print(string)
