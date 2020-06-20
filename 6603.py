import sys
from itertools import combinations

cnt = 0
while True:
    numarr=list(map(int,sys.stdin.readline().split()))
    k=numarr[0]
    numarr=numarr[1:]
    if k == 0:
        exit()

    else:
        if cnt!=0:
            print()
        result=[]
        for case in list(combinations(numarr,6)):
            result.append(list(case))

            # result.sort()
            # for i in result:
            #     print(i,end=' ')
        result.sort()
        for temp in result:
            temp.sort()
            for j in temp:
                print(j,end=' ')
            print()
    cnt+=1