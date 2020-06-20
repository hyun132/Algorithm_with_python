def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)


case=input()
sumarr=[]
for i in range(0,int(case)):

    arr = list(map(int,input().split()))
    sum=0
    for n in range(1,len(arr)-1):
        for m in range(n+1,len(arr)):
            if arr[n]>arr[m]:
                sum=sum+gcd(arr[n],arr[m])
            else:
                sum = sum + gcd(arr[m], arr[n])
    sumarr.append(sum)
    arr=[]
for k in sumarr:
    print(k)