import re


def solution(phone_book):
    phone_book.sort(key=lambda x:len(x))
    print(phone_book)

    idx=1
    for nums in phone_book[:-1]:
        for i in range(idx,len(phone_book)):
            p=re.compile('^'+nums)
            if p.match(phone_book[i])!=None:
                print(False)
                return False
        idx+=1
    print(True)
    return True

solution(["119", "97674223", "1195524421","22"])
# solution(["123","456","789"])