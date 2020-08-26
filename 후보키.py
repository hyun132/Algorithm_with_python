from itertools import combinations
def solution(relation):
    answer=[]
    keys=[]
    for j in range(1,len(relation)):
        keys.extend(map(list,combinations([i for i in range(len(relation[0]))],j)))

    for _ in range(len(keys)):
        for key in keys:
            tempSet=set()
            for y in range(len(relation)):
                temp=''
                for idx in key:
                    temp = temp+ relation[y][idx]
                tempSet.add(temp)

            if len(tempSet)==len(relation):
                if key not in answer:
                    answer.append(key)
            tempSet.clear()

    answer.sort(key= lambda x:len(x))
    realAnswer=answer[:]
    for i in range(len(answer)-1):
        for j in range(i+1,len(answer)):
            cnt=0
            for a in answer[i]:
                if a in answer[j]:
                    cnt+=1
            if cnt==len(answer[i]):
                if answer[j] in realAnswer:
                    realAnswer.remove(answer[j])
    return len(realAnswer)




solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])