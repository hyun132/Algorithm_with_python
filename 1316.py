import sys

num=int(sys.stdin.readline().strip())

cnt=num
temp=set()
for _ in range(num):
    word=sys.stdin.readline().strip()

    temp.clear()
    # print(cnt)
    i=0
    while i<len(word):
        # print(word[i])
        if word[i] in temp:
            cnt -= 1
            break
        elif word[i] not in temp:
            temp.add(word[i])
            while True:
                if i+1>=len(word):
                    break
                if word[i]== word[i+1]:
                    i+=1
                else:
                    break
        i+=1


print(cnt)

