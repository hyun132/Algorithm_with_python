def solution(clothes):
    types = dict()

    for item,type in clothes:
        if type in types:
            types[type]+=1
        else:
            types[type]=1

    answer=1
    for num in types.values():
        answer*=(num+1)

    print(answer-1)
    return answer-1


# solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])