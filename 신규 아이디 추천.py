import re


def solution(new_id):
    new_id=new_id.lower()

    p=re.compile('[-_.0-9a-z]')
    new_id=''.join(p.findall(new_id))

    # . 연속되는 부분 걸러내기
    dot = '.'*14
    for i in range(1,14):
        new_id=new_id.replace(dot,'.')
        dot=dot[:-1]

    new_id = new_id.strip('.')


    if len(new_id)==0 or new_id=='':
        new_id='a'

    if len(new_id)>15:
        new_id=new_id[:15]
        while new_id[-1]=='.':
            new_id = new_id.rstrip('.').strip()

    while len(new_id) < 3:
        if len(new_id)<3:
            new_id=new_id + new_id[-1]

    return ''.join(new_id).strip('.')



# solution("...!@BaT#*..y.abcdefghijklm")
# solution("z-+.^.")
# solution("=.=")
# solution('--.-a')
# solution('tttttttttttTTtt')