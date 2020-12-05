#계단오르기


n=int(input())
stairs = [0]+[int(input()) for _ in range(n)]
if n>3:
    dp=[0,stairs[1],stairs[1]+stairs[2]]+[0]*(n-2)

    for i in range(3,n+1):
        dp[i]=(max(dp[i-3]+stairs[i-1],dp[i-2])+stairs[i])

    print(dp[n])
else:
    if n==1:
        print(stairs[n])
    elif n==2:
        print(sum(stairs))
    else:
        print(max(stairs[0],stairs[1])+stairs[2])
