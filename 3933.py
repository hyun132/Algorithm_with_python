import sys
input = sys.stdin.readline

k = 2**15
issquare = [0] * (k)
square = []
for i in range(2**8):
    m = i ** 2
    if m >= k:
        break
    square.append(m)
    issquare[m] = 1
print(issquare)
def lagrange(n, m, k = 4):
    if k == 1:
        return issquare[n]
    bd = n // k
    s = 0
    k -= 1
    for i in range(m, n):
        x = square[i]
        if x > bd:
            break
        s += lagrange(n-x, i, k)
    return s

while True:
    n = int(input())
    if n:
        print(sum(lagrange(n, 1, k) for k in range(1, 5)))
    else:
        break