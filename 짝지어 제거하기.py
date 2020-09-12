def solution(s):
    stack=[]

    if len(s)==1:
        return 0

    for ch in s:
        if len(stack)==0:
            stack.append(ch)
            continue
        if stack[-1]==ch:
            stack.pop()
        else:
            stack.append(ch)

    if len(stack)==0:
        print(1)
        return 1
    else:
        alph=set(s)
        for ch in alph:
            if s.count(ch)>1:
                print(0)
                return 0
        print(1)
        return 1

# def solution(s):
#     alph=set(s)
#
#     if len(s)%2==1:
#         return 0
#
#     while True:
#         temp=s[:]
#         print(temp)
#         for ch in alph:
#             s=s.replace(ch+ch,'')
#
#         if len(s)==len(temp):
#             for a in alph:
#                 if s.count(a)>1:
#                     print(0)
#                     return 0
#             return 1


solution("a")