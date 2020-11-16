import re
tempset=set()

def fun(idx,caseArr,visited):
    global tempset
    if idx==len(caseArr):
        if len(visited) == len(set(visited)):
            visited.sort()
            tempset.add(tuple(visited))
        return

    for id in caseArr[idx]:
        fun(idx+1,caseArr,visited+[id])

def solution(user_id, banned_id):
    caseArr = []
    global tempset
    for id in banned_id:
        splited_id=id.replace('*','.')
        p=re.compile(splited_id)

        temparr=[]
        for user in user_id:
            if p.match(user)!=None and len(id)==len(user):
                temparr.append(user)
            # print(temparr)
        caseArr.append(temparr)

    fun(0,caseArr,[])

    return len(tempset)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
