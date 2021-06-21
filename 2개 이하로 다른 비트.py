# 그냥 1씩 더해서 구하는 방법은 시간초과
# 따라서 홀수 짝수에 따라 마지막 0을 1로 바꿔주는 방법으로 풀이.
def solution(numbers):
    answer = []

    for num in numbers:
        temp = list('0'+ bin(num)[2:])
        idx = ('0'+ bin(num)[2:]).rfind('0')
        if num%2==1:
            temp[idx+1]='0'
        temp[idx]='1'

        answer.append(int(''.join(temp),2))

    # print(answer)
    return answer

# 아래의 풀이는 다른 사람의 풀이로, 바이너리 연산을 이용한 풀이인데 가장 최적의 풀이라고 한다.
# def solution(numbers):
#     answer = []
#     for idx, val in enumerate(numbers):
#         print((val+1) >> 2)
#         print(((val ^ (val+1)) >> 2))
#         print(((val ^ (val+1)) >> 2) +val +1)
#         answer.append(((val ^ (val+1)) >> 2) +val +1)
#         print()
#     return answer

solution([2, 7])
