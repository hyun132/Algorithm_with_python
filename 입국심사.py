
def solution(n, times):

    times=sorted(times)

    l=0
    r=times[-1]*n
    answer=0
    while l<=r:
        mid=(l+r+1)//2
        temp=0
        for time in times:
            temp+=(mid//time)
            if temp>n:
                break

        if temp>=n:
            r=mid-1
            answer = mid

        else:
            l=mid+1

    print(mid)



    # take_time_arr=[times[j] for j in range(len(times))]
    #
    # for i in range(n):
    #
    #     idx = take_time_arr.index(min(take_time_arr))
    #     take_time_arr[idx]=take_time_arr[idx]+times[idx]
    #
    # for k in range(len(times)):
    #     take_time_arr[k]=take_time_arr[k]-times[k]

    # return max(take_time_arr)


solution(6,[7,10])