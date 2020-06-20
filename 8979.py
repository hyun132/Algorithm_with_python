import sys

n,r=map(int,sys.stdin.readline().strip().split())

data=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

data.sort(key=lambda x:(x[1],x[2],x[3]),reverse=True)


# print(data)
for i in range(len(data)):
    if data[i][0]==r:
        for item in enumerate(data[i-1::-1]):
            # print(item)
            if data[i][3] != item[1][3] or data[i][2] != item[1][2] or data[i][1] != item[1][1] :
                print(i+1-item[0])
                exit()
        #     # print(data)