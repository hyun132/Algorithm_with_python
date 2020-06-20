import sys

a,b=sys.stdin.readline().strip().split()
# print(a,b)

arra=""
arrb=""
for i in range(len(a)-1,-1,-1):
    arra=arra+a[i]
    arrb=arrb+b[i]

if int(arrb)>int(arra):
    print(arrb)
else:
    print(arra)





