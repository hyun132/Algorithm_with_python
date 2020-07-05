import re


def solution(genres, plays):

    gendict=dict()
    numOfPlay=0
    for i in range(len(genres)):
        if genres[i] in gendict:
            gendict[genres[i]].append(plays[i])
        else:
            gendict[genres[i]]=[plays[i]]

    gendict = sorted(gendict.items(),key= lambda x:sum(x[1]),reverse=True)
    print(gendict[0])
    used=[False]*len(plays)
    answer = []
    for item in gendict:
        # print(item)
        arr=sorted(item[1],reverse=True)
        for i in range(min(len(arr),2)):
            for j in range(len(plays)):
                if plays[j]==arr[i] and genres[j]==item[0] and used[j]==False:
                    answer.append(j)
                    used[j]=True
                    break

    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])