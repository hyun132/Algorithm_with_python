import sys

def calc(resultoparr,val,d):
    global maxval, minval
    if d==len(numarr):
        if maxval<val:
            maxval=val
        if minval>val:
            minval=val
        return
    for i in range(4):
        tempop = resultoparr[:]
        if resultoparr[i] == 0:
            continue
        tempop[i] -= 1
        if i == 0:
            calc(tempop,val+numarr[d],d+1)
        elif i == 1:
            calc(tempop,val-numarr[d],d+1)
        elif i == 2:
            calc( tempop,val*numarr[d],d+1)

        elif i == 3:
            if val>0:
                calc( tempop,val//numarr[d],d+1)
            else:
                calc( tempop, -(-val // numarr[d]), d+1)
    return

N=int(sys.stdin.readline().strip())
numarr=list(map(int,sys.stdin.readline().strip().split()))
oparr=list(map(int,sys.stdin.readline().strip().split()))
result=[]
maxval = -sys.maxsize
minval = sys.maxsize
def main():

    calc(oparr,numarr[0],1)
    print(maxval)
    print(minval)
main()