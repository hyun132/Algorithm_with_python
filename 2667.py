import sys

def fun():
    n=int(sys.stdin.readline())
    arr=[]
    for i in range(n):
        temp=sys.stdin.readline().strip()
        row=[]
        for str in temp:
            row.append(str)
        arr.append(row)
    num=0
    count=[]
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='1':
                count.append(search(arr,i,j,1))
                num=num+1

    print(num)
    count.sort()
    for i in count:
        print(i)

def search(arr,x,y,count):
    arr[x][y] = '0'
    dn=[[x,y+1],[x,y-1],[x-1,y],[x+1,y]]

    for dx,dy in dn:
        if len(arr)>dx>=0 and len(arr)>dy>=0:
            if arr[dx][dy]=='1':

                count = search(arr,dx,dy,count+1)
    return count

fun()