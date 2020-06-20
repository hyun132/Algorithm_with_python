import sys


def sol(count):
    result=0
    for r in range(count):
        arr=list(map(str,sys.stdin.readline().split()))
        if len(arr)>1:
            num=int(arr[1])-1
            cal = arr[0]
            if cal=='check':
                if result&1<<num!=0:
                    print(1)
                else:
                    print(0)
            elif cal=='add':
                result|=1<<num
            elif cal=='remove':
                # print("remove",result)
                result&=~(1<<num)
                # print("removed",result)
            elif cal=='toggle':
                # print("toggle",result)
                result^=1<<num
                # print("toggled",result)
        else:
            cal = arr[0]
            if cal=='all':
                result=(1<<21)-1
            elif cal =='empty':
                result=0

        # print("cal",cal, "result",result)


count=input()

sol(int(count))