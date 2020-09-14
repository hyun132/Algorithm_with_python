def solution(n):
    cnt=1

    while n>1:
        cnt+=n%2
        n//=2

    print(cnt)


# solution(5)
# solution(6)
solution(5000)
