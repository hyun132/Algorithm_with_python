n=int(input())

mem = dict()

def move(s,e,num):
    arr=[]
    if num==1:
        return [(s,e)]
    if (s,6-s-e,num-1) in mem:
        arr.extend(mem[(s,6-s-e,num-1)])
    else:
        temp1 = move(s,6-s-e,num-1)
        arr.extend(temp1)
        mem[(s,6-s-e,num-1)]=temp1

    arr.extend([(s,e)])

    if (6-s-e,e,num-1) in mem:
        arr.extend(mem[(6-s-e,e,num-1)])
    else:
        temp = move(6-s-e,e,num-1)
        arr.extend(temp)
        mem[(6-s-e,e,num-1)]=temp

    return arr

answer=move(1,3,n)
print(len(answer))
for s,e in answer:
    print(s,end=" ")
    print(e)