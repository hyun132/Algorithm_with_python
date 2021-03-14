from itertools import combinations
import collections
import itertools

def solution(orders, course):
    menus=[dict() for _ in range(20)]

    answer=[]

    for order in orders:
        for num in course:
            if num<2:
                continue
            order=sorted(order)
            for case in list(combinations(order,num)):
                if len(case)<2:continue
                if case in menus[num]:
                    menus[num][case]+=1
                else:
                    menus[num][case]=1

    for menudict in menus:
        if len(menudict)>0:
            menudictarr = sorted(menudict, key=lambda x:menudict[x],reverse=True)

            maxval = menudict[menudictarr[0]]
            if maxval<2: continue
            answer.append("".join(menudictarr[0]))
            for i in range(1,len(menudict)):
                if maxval>menudict[menudictarr[i]]: break
                else:
                    answer.append("".join(menudictarr[i]))

    print(sorted(answer))

# 참조한 좋은 풀이
def solution2(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])