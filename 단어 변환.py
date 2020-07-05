from collections import deque


def bfs(start,target, words):
    # visited = [False] * len(words)
    q=deque()
    q.append(start)
    turn=0

    while q:
        size=len(q)
        for i in range(size):
            node=q.popleft()
            for word in words:
                cnt =0
                for ch1,ch2 in zip(word,node):
                    if ch1 != ch2:
                        cnt+=1
                    if cnt>1:
                        break
                if cnt==1:
                    if word == target:
                        print(word, turn+1)
                        return turn+1
                    q.append(word)
                    words.pop(words.index(word))
        turn+=1

    return turn

def solution(begin, target, words):

    if target not in words:
        return 0

    return bfs(begin,target,words)

# solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])
solution("hit","cog",["hot", "dot", "dog", "lot", "log"])