def getLength(s,idx):
    l=idx-1
    r=idx+1
    if s[l]!=s[r]:
        return 0
    while True:
        if (l<0 or r>=len(s)) or s[l]!=s[r]:
            return (r-idx)*2-1
        l-=1
        r+=1

def getLengthEven(s,idx):
    l=idx
    r=idx+1
    if s[l]!=s[r]:
        return 0
    while True:
        if (l<0 or r>=len(s)) or s[l]!=s[r]:
            print(idx,l+1,r-1)
            return (r-1)-(l+1)+1
        l-=1
        r+=1


def solution(s):
    maxLen=0

    if len(s)==s.count(s[0]):
        print(len(s))
        return len(s)

    for i in range(1,len(s)-1):
        maxLen=max(maxLen,getLength(s,i),getLengthEven(s,i-1))

    if maxLen==0:
        return 1
    return maxLen

solution("abcd")