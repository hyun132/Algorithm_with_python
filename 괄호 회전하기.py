def solution(s):
    count=0
    for i in range(len(s)):
        if fun(s[i:]+s[:i]):
            count+=1

    return (count)

def fun(arr):

    brArr=dict()
    brArr['}']="{"
    brArr[')']="("
    brArr[']']="["

    stack=[]
    for bracket in arr:
        if len(stack)==0 or bracket not in brArr.keys() or stack[-1] != brArr[bracket]:
            stack.append(bracket)
        elif stack[-1]== brArr[bracket]:
            stack.pop()

    if len(stack)>0:
        return False
    return True