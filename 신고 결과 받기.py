from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    users = dict()
    for idx, user_id in enumerate(id_list):
        users[user_id] = idx

    reporters = defaultdict(list)
    for row in set(report):
        reporter, bad_user = row.split(' ')
        reporters[bad_user].append(reporter)

    for key,value in reporters.items():
        if len(value) >= k:  # 정지 대상이면
            for user in value:
                answer[users[user]] += 1

    return answer


# solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
solution(["muzi", "frodo", "apeach", "neo"]	,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2)