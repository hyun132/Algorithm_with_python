def solution(n):
    num=bin(n)
    one=num.count('1')
    for i in range(1,100000):
        if list(bin(n+i)[:1:-1]).count('1') == one:
            answer=n+i
            break
    print(answer)

solution(78)