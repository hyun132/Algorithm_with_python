def solution(clothes):

    cat=dict()
    for item in clothes:
        if item[1] in cat.keys():
            cat[item[1]].append(item[0])
        else:
            cat[item[1]]=[item[0]]
    # print(cat)
    answer=1
    for item in cat.keys():
        # print(len(cat[item])+1)
        answer*=(len(cat[item])+1)

    print(answer-1)
    return answer-1
# solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])