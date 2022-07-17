N,M = map(int,input().strip().split())
print(N,M)
answer = N
for i in range(N+1,M+1):
    answer = answer ^ i

print(bin(answer))