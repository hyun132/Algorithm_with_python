n=int(input())

for _ in range(n):
    sub1=[1,0] # n-2
    sub2=[0,1] # n-1
    num=int(input())
    if num==0:
        print(sub1[0],sub1[1])
    elif num==1:
        print(sub2[0],sub2[1])
    else:
        for i in range(3,num+1):
            sub1,sub2 = sub2,[sub2[0]+sub1[0],sub2[1]+sub1[1]]

        print(sub2[0]+sub1[0],sub2[1]+sub1[1])
