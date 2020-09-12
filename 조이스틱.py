# def getCnt(name,arr,answer):
#     idx=0
#     cnt=0
#
#     while sum(arr)!=0:
#         cnt+=arr[idx]
#         arr[idx]=0
#
#         if arr[(idx+1+len(name))%len(name)]>=arr[(idx-1+len(name))%len(name)]:
#             idx=(idx+1+len(name))%len(name)
#         else:
#             idx=(idx-1+len(name))%len(name)
#
#         print(idx)
#         cnt+=1
#
#     answer.append(cnt)
#     print(cnt)

def solution(name):
    idx=0
    cnt=0
    arr=[]
    for alphbet in name:
        alphbet=ord(alphbet)
        arr.append(min(91 - alphbet, alphbet - 65))

    while sum(arr)!=0:
        rIdx=(idx+1+len(name))%len(name)
        lIdx=(idx-1+len(name))%len(name)

        cnt+=arr[idx]
        arr[idx]=0

        if sum(arr)==0:
            break

        for i in range(len(name)):
            cnt += 1
            if arr[(lIdx - i + len(name)) % len(name)] != 0:
                idx = (lIdx - i + len(name)) % len(name)
                break
            elif arr[(rIdx+i+len(name))%len(name)]!=0:
                idx=(rIdx+i+len(name))%len(name)
                break



    # answer.append(cnt)
    print(cnt)

# def solution(name):
#     answer=[]
#     arr=[]
#     for alphbet in name:
#         alphbet=ord(alphbet)
#         arr.append(min(91 - alphbet, alphbet - 65))
#
#
#     getCnt(name,arr,answer)
#     getCnt2(name, arr, answer)
#     getCnt(name[0]+name[::-1][:-1], [arr[0]]+arr[::-1][:-1], answer)
#     getCnt2(name[0] + name[::-1][:-1], [arr[0]]+arr[::-1][:-1], answer)
#
#     print(answer)

# solution("JEROEN")
# solution("JAN")
# solution("BBBAAAB")
# solution("ABABAAAAABA")
solution("ABBAAAAAB")