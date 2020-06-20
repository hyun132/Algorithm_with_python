import sys

num=int(sys.stdin.readline().strip())

word1=sys.stdin.readline().strip()




result=0
size=len(word1)
cnt = 0
for _ in range(num-1):

    # check = [-1 for _ in range(size + 1)]
    check = dict()
    check['notin'] = 0
    for i in range(len(word1)):
        if word1[i] not in check:
            check[word1[i]] = -1
        else:
            check[word1[i]] -= 1

    word2 = sys.stdin.readline().strip()
    # print(check)
    for i in range(len(word2)):
        if word2[i] in check.keys():
            check[word2[i]]+=1
        else:
            check['notin']+=1
    # print(word2)
    # print(check)

    sum=0
    sum2=0
    # print(word2)
    # print(check)
    for i in check.values():
        if i<0:
            sum2+=-i
        else:
            sum+=i
    if sum2>1 or sum>1:
        cnt+=1
        # print(word2)

    check.clear()

print(num-cnt-1)

