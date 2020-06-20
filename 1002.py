import math
import sys

case=int(sys.stdin.readline().strip())

for _ in range(case):
    ax,ay,ar,bx,by,br=list(map(int,sys.stdin.readline().split()))
    d=((ax-bx)**2+(ay-by)**2)**0.5

    if max(ar,br)>=d:
        if ax==bx and ay==by and ar==br:
            print(-1)
        elif min(ar,br)+d==max(ar,br):
            print(1)
        elif min(ar,br)+d<max(ar,br):
            print(0)
        elif min(ar,br)+d>max(ar,br):
            print(2)
    else:
        if ar+br>d:
            print(2)
        elif ar+br==d:
            print(1)
        elif ar+br<d:
            print(0)



    # for i in range(10000):
    #     if (ax-bx)**2+(ay-by)**2<ad+bd or (ax-bx)**2+(ay-by)**2 + min(ad,bd)<max(ad,bd):
    #         print(0)
    #         continue
    #     if (ax-bx)**2+(ay-by)**2<ad+bd or (ax-bx)**2+(ay-by)**2 + min(ad,bd)==max(ad,bd):
    #         print(1)
    #         continue





    # cnt=0
    # for x in range(10000):
    #     y=(ad**2-x**2)**0.5
    #     if ax-ad<= x <=ax+ad:
    #         if ay-ad<= (ad ** 2 - x ** 2) ** 0.5 <=ay+ad:
    #
    #
    #     if cnt==2:
    #         break



    # if ax==bx and ay==by and (La!=Lb):
    #     print(0)
    #     continue

    flag=0
    # if La!=0 and Lb!=0:
    #     for x in range(10000):
    #         print(La**2-(x-ax))
    #         y=(math.sqrt(La**2-(x-ax))-ay)
    #         y=(-y)
    #         if (bx-x)**2 + (by-y)**2 == Lb**2:
    #             print(2)
    #             flag=1
    #             break
    #         if ax-bx==0 or x!=0:
    #             if (ay-by)/1 == y/x:
    #                 print(1)
    #                 flag=1
    #                 break
    #         elif x==0 or ax-bx!=0:
    #             if (ay-by)/(ax-bx) == y:
    #                 print(1)
    #                 flag=1
    #                 break
    #         else:
    #             if (ay-by)/(ax-bx) == y/x:
    #                 print(1)
    #                 flag=1
    #                 break
    # if flag==0:
    #     print(0)
    #
    #
    # if flag==0:
    #     print(2)



