import re
from itertools import permutations


def solution(expression):

    op=['*','+','-']
    cases = list(permutations(op, 3))
    numpatter=re.compile('(\d{1,3})')
    oppattern=re.compile('[-*+]')
    answer=[]

    for case in cases:
        numarr = numpatter.findall(expression)
        oparr = oppattern.findall(expression)

        numstack=[numarr[0]]
        numarr=numarr[1:]
        opstack=[]
        for o in case:
            for num,op in zip(numarr,oparr):
                if o=='+':
                    if op == o:
                        numstack.append(int(numstack.pop())+int(num))
                    else:
                        numstack.append(num)
                        opstack.append(op)
                if o=='-':
                    if op == o:
                        numstack.append(int(numstack.pop())-int(num))
                    else:
                        numstack.append(num)
                        opstack.append(op)
                if o=='*':
                    if op == o:
                        numstack.append(int(numstack.pop())*int(num))
                    else:
                        numstack.append(num)
                        opstack.append(op)

            if len(numstack)==1:
                answer.append(abs(numstack[0]))
                break
            numarr=numstack[1:]
            oparr=opstack[:]
            numstack=[numstack[0]]
            opstack=[]

    print(max(answer))


solution("100-200*300-500+20")