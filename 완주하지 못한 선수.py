from collections import Counter


def solution(participant, completion):
    cntp=Counter(participant)
    cntc = Counter(completion)
    for name in cntp.keys():
        if cntc[name]==cntp[name]:
            continue
        else:
            print(name)
            break
    # print(cntp)
    # result=set(participant)-set(completion)
    # result=list(result)
    # print(list(result)[0])
    # return result[0]

solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])