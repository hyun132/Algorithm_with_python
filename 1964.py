n = input()
n=int(n)
dots=5
for i in range(2,n+1):
    dots=dots+3*i+1


print(dots%45678)