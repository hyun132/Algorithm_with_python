def solution(s):
    answer = []
    s=s[2:-2]
    s=s.split('},{')
    for idx in range(len(s)):
        s[idx]=list(map(int,s[idx].split(',')))

    s.sort(key=lambda x:len(x))

    for i in s[0]:
        answer.append(i)

    for y in range(1,len(s)):
        for x in s[y]:
            if x in answer:
                continue
            answer.append(x)
    return answer


# solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
# solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")
# solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")