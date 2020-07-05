from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = []
    cnt=[]
    total_time=1
    bridge.append(truck_weights[0])
    cnt.append(1)
    for i in range(1,len(truck_weights)):
        # print(i,total_time, cnt, bridge)
        if cnt[0]==bridge_length:
            cnt.pop(0)
            bridge.pop(0)
        if sum(bridge)+truck_weights[i]>weight:
            # print(sum(bridge)+truck_weights[i], weight, "++++++++++++++")
            while True:
                time=bridge_length-cnt[0]
                total_time+=(time)
                cnt.pop(0)
                bridge.pop(0)
                for j in range(len(bridge)):
                    cnt[j]+=(time)
                if sum(bridge) + truck_weights[i] <= weight:
                    break

        total_time+=1
        for j in range(len(bridge)):
            cnt[j]+=1

        bridge.append(truck_weights[i])
        cnt.append(1)
        # print(total_time, cnt, bridge)
    # print(total_time, cnt, bridge)
    # 마지막 트럭 남은 시간 더해줌
    if bridge:
        total_time += (bridge_length - cnt[-1])
        cnt.pop(0)
        bridge.pop(0)
    print(total_time+1)
    return total_time+1
    # answer = 0
    # return answer

solution(2, 10, [7,4,5,6])
# solution(100,100,[10])
# solution(100,100,[10,10,10,10,10,10,10,10,10,10])
# solution(5,5,[1, 1, 1, 1, 1, 2, 2, 2, 2])
# solution(7,7,[1, 1, 1, 1, 1, 3, 3])