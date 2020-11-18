def solution(n):
    arr=[0,1,2,3]+[0]*(n-2)

    if n<4:
        return(arr[n])

    for i in range(4,n+1):
        arr[i]=arr[i-1]+arr[i-2]

    return(arr[n]%1234567)

def solution2(n):
    a = 0
    b = 1
    for i in range(1, n + 1):
        a, b = b, a + b

    return (b % 1234567)

solution(4)