import sys

case=int(sys.stdin.readline().strip())
for _ in range(case):
    num=int(sys.stdin.readline().strip())

    arr=[0]+list(map(int,sys.stdin.readline().split()))
    visited=[0]*(num+1)

    group=1
    for i in range(1,num+1):
        # 연결된 노드 방문
        if visited[i]==0:
            # 만약 방문했던 노드 다시 방문하면 종료
            while visited[i]==0:
                visited[i]=group
                i=arr[i]
            #     만약 방문했던 노드의 그룹이 지금 그룹 번호와 같으면 =>싸이클 -1로 표시
            while visited[i]==group:
                visited[i]=-1
                i=arr[i]
        group+=1
        # print(visited)
    cnt=0

    for i in visited:
        if i>0:
            cnt+=1
    sys.stdout.write("{}\n".format(cnt))

# import sys
# testcase = int(sys.stdin.readline())
# for _ in range(testcase):
#     n = int(sys.stdin.readline())
#     choice = [0] + list(map(int, sys.stdin.readline().split()))
#     visit = [0] * (n+1)
#     group = 1
#     for i in range(1, n+1):
#         if visit[i] == 0:
#             while visit[i] == 0:
#                 visit[i] = group
#                 i = choice[i]
#             while visit[i] == group:
#                 visit[i] = -1
#                 i = choice[i]
#         group += 1
#     cnt = 0
#     for v in visit:
#         if v > 0:
#             cnt += 1
#     sys.stdout.write("{}\n".format(cnt))
