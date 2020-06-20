import sys
from math import ceil

inputarr=sys.stdin.readline().strip()

# numarr=[]
cnt=[0 for _ in range(10)]
for i in range(len(inputarr)):
    cnt[int(inputarr[i][0])] += 1
    # print(inputarr[i][0])
    # numarr.append()


# print(cnt)
# for num in numarr:
#     cnt[num]+=1

cnt[6]=cnt[9]=ceil((cnt[6]+cnt[9])/2)
# print(cnt)
print(max(cnt))