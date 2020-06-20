# num=dict()

# num[3]='ABC'
# num[4]='DEF'
# num[5]
import sys

num=sys.stdin.readline().strip().split()

sum=0
for c in num[0]:
    if c in 'ABC':
        sum+=3
    elif c in 'DEF':
        sum+=4
    elif c in 'GHI':
        sum+=5
    elif c in 'JKL':
        sum+=6
    elif c in 'MNO':
        sum+=7
    elif c in 'PQRS':
        sum+=8
    elif c in 'TUV':
        sum+=9
    elif c in 'WXYZ':
        sum+=10

print(sum)