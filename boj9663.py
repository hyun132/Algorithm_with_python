n=int(input())

answer=0
row=[0] * n
dig1=[0] *(2*n-1) # ↗↙ 요 대각선의 갯수
dig2=[0]*(2*n-1)  # ↖↘ 이 방향 대각선의 갯수

def fun(y):
    global answer
    if y==n:
        answer+=1
        return
    else:
        for x in range(n):
            # 각 방향의 대각선의 칸들의 규칙을 찾으면 ↗↙방향의 같은라인 칸은 y+x 값 이 같음,
            # ↖↘ 이 방향은 y-x 에 정수를 만들기위해 n-1을 더해서y - x + n - 1
            # 한 줄에 퀸이 한개밖에 놓일 수 없으므로 가로세로 중 하나 (나는 row)를 검사
            if(row[x]==0 and dig1[y-x+n-1]==0 and dig2[y+x]==0):
                row[x]=1
                dig1[y-x+n-1]=1
                dig2[y + x] =1
                fun(y+1)
                row[x] = 0
                dig1[y - x + n - 1] = 0
                dig2[y + x] = 0

fun(0)
# print()
print(answer)