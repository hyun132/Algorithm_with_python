import sys

name=sys.stdin.readline().split('-')
for i in range(len(name)):
    print(name[i][0],end='')
