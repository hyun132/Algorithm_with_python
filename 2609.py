N,M=map(int, input().split())
arr=[]

def fun(a,b):

    if b==0:
        return a

    if a<b:
        temp=b
        b=a
        a=temp

    return fun(b,a%b)

gcd=fun(N,M)
lcm=N*M//gcd
print(gcd)
print(lcm)