import sys


def fun(change,cnt):
    moneyarr = [500, 100, 50, 10, 5, 1]
    for temp in moneyarr:
        if change//temp < 1:
            continue
        cnt = cnt + (change // temp)
        change-=(change//temp)*temp

        # print(temp)

    print(cnt)

change=1000-int(sys.stdin.readline().strip())

fun(change,0)