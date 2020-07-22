def solution(people, limit):

    # minWeight=min(people)
    people.sort()
    i=0
    count=0
    idx = len(people) - 1
    while True:
        if i==idx:
            count+=1
            break
        while people[idx]+people[i]<=limit:
            if i>=idx:break
            count+=1
            idx -= 1
            i += 1

        while people[idx]> limit-people[i] and i<idx:
            if i >= idx: break
            idx-=1
            count+=1

        if i>idx:
            break


    print(count)
    return count

# solution([70, 50, 80, 50],100)
solution([70, 80, 50],100)