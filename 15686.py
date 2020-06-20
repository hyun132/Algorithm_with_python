import sys
from itertools import combinations

board=[]
size,select=map(int,sys.stdin.readline().strip().split())

house=[]
chicken=[]
for y in range(size):
    row = list(map(int,sys.stdin.readline().strip().split()))
    for x in range(size):
        if row[x]==1:
            house.append((y,x))
        elif row[x]==2:
            chicken.append((y,x))

result=[]
for seledted in combinations(chicken,select):
    tempdis=0
    for hy,hx in house:
        dis=99
        for cy,cx in seledted:
            dis=min(dis,abs(hy-cy)+abs(hx-cx))
        tempdis=tempdis+dis
    result.append(tempdis)

print(min(result))
