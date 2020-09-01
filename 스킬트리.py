import re


def solution(skill, skill_trees):
    alph=dict()
    cnt=0
    isTrue=''
    for i in range(len(skill)):
        isTrue+=str(i)
    print(isTrue)
    for idx,alphbet in enumerate(skill):
        alph[alphbet] =str(idx)

    for skill_ in skill_trees:
        temp=''
        for ch in skill_:
            if ch in alph:
                temp+=alph[ch]
        if temp==isTrue[:len(temp)]:
            cnt+=1

    print('\n'+str(cnt))
    return cnt


solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])