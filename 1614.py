import sys

f=int(sys.stdin.readline().strip())
c=int(sys.stdin.readline().strip())
#
# cnt=0
# sum=1
#
if c==0:
    print(f-1)
    exit()
# while True:
#     for i in range(1,5):
#         if i == f:
#             if cnt==c:
#                 print(sum)
#                 exit()
#             cnt+=1
#         sum+=1
#     for i in range(4,0,-1):
#         if i == f:
#             if cnt==c:
#                 print(sum)
#                 exit()
#             cnt+=1
#         sum += 1

if f==1:
    print(8*c)
elif f==3:
    print(2 + 4 * c)
elif f==5:
    print(4+8*c)
elif f==2:
    if c%2==0:
        print(4*c+1)
    else:
        print(4*c+3)
else:
    if c % 2 == 0:
        print(4*c+3)
    else:
        print(4*c+1)
