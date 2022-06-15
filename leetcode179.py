from functools import cmp_to_key


def largestNumber(nums):
    print(str(int("".join(map(str, sorted(nums, key=cmp_to_key(compare)))))))


def compare(a, b):
    a = str(a)
    b = str(b)
    a, b = a + b, b + a
    if a < b:
        return 1
    else:
        return -1


def compare2(a, b):
    a = str(a)
    b = str(b)
    diff = len(a) - len(b)
    a, b = a + b, b + a
    for a_num, b_num in zip(a, b):
        if a_num < b_num:
            return 1
        elif a_num > b_num:
            return -1
    if diff > 0:
        return 1
    elif diff == 0:
        return 0
    else:
        return -1


# largestNumber([3, 30, 34, 5, 9])
largestNumber([10, 2])
# largestNumber([8308,8308,830])
# largestNumber([0, 0])
