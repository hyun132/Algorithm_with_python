def turn(keyPosition,size):
    newKey=[]
    for y,x in keyPosition:
        newKey.append([size-x,y])
    return newKey

def isFit(toFillOut,key,keyPosition,lock):

    for i in range(-len(key),len(lock)):
        for j in range(-len(key),len(lock)):
            temp = [p for p in toFillOut]
            notUsed=[]
            for dy,dx in keyPosition:
                if [dy+i,dx+j] in temp:
                    temp.remove([dy+i,dx+j])
                else:
                    notUsed.append([dy+i,dx+j])
                    # if 0<=dy+i<len(lock) and 0<=dx+j<len(lock) and :
                    #     break
            if temp==[]:
                flag=0
                for one in notUsed:
                    if 0<=one[0]<len(lock) and 0<=one[1]<len(lock):
                        flag=1
                        break
                if flag==0:
                    return True

    return False


def solution(key, lock):

    toFillOut=[]
    for y in range(len(lock)):
        for x in range(len(lock)):
            if lock[y][x]==0:
                toFillOut.append([y,x])

    keyPosition =[]
    for y in range(len(key)):
        for x in range(len(key)):
            if key[y][x]==1:
                keyPosition.append([y,x])

    for i in range(4):
        keyPosition=turn(keyPosition,len(key)-1)
        if isFit(toFillOut, key, keyPosition, lock)==True:
            print(True)
            return True

    print(False)
    return False

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])