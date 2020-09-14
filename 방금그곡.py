def newmelody(melody):
    melody=melody.replace('C#', 'H')
    melody=melody.replace('D#', 'I')
    melody=melody.replace('F#', 'J')
    melody=melody.replace('G#', 'K')
    melody=melody.replace('A#', 'L')
    return melody.strip()

def solution(m, musicinfos):
    m=newmelody(m)
    answer=[]
    for idx,info in enumerate(musicinfos):
        start,end,title,melody = info.split(',')
        melody=newmelody(melody)

        sh,sm = list(map(int,start.split(':')))
        eh,em = list(map(int,end.split(':')))

        duration=(eh-sh)*60+(em-sm)

        if duration>len(melody):
            idx = 0
            while len(melody)<duration:
                melody+=melody[idx]
                idx+=1

            if m in melody:
                answer.append([duration,idx,title])
        else:
            if m in melody[0:duration]:
                answer.append([duration, idx, title])

    if answer==[]:
        return '(None)'
    maxlen=0
    maxtitle=''
    for item in answer:
        if maxlen<item[0]:
            maxtitle=item[2]
            maxlen=item[0]

    return maxtitle