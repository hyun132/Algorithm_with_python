def solution(n, words):
    last=''
    cnt=[0]*n
    already=set()
    for idx, word in enumerate(words):
        if last=='':
            last=word[-1]
            cnt[idx%n]+=1
            already.add(word)
            continue
        if last!=word[0] or word in already:
            print([idx % n +1 ,cnt[idx % n] + 1])
            return [idx % n +1 ,cnt[idx % n] + 1]
        else:
            last = word[-1]
            cnt[idx % n] += 1
            already.add(word)

    return [0,0]

solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])