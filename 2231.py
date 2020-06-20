N=input()

size=len(N)
N=int(N)

maxcase=9*size

def fun():
    if N<10:
        return 0
    for i in range(N-maxcase,N+1):
        a=str(i)
        sum=0
        # for j in a:
        #     sum=sum+int(j)
        for j in a:
            sum=sum+int(j)
        if sum+i == N:
            return i
    return 0

print(fun())