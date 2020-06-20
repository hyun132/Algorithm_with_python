def find(x):
    global count
    if len(map[x]) == 0:
        count = count + 1
    else:
        for i in map[x]:
            find(i)

count = 0;
n = int(input())
l = list(map(int, input().split()))
map = [[] for _ in range(52)]
for _ in range(0, n):
    if (l[_] == -1):
        start = _
    else:
        map[l[_]].append(_)
t = int(input())
for i in range(n):
    if t in map[i]:
        map[i].remove(t)
if start != t:
    find(start)
print(count)