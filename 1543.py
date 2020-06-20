import re
import sys

doc=sys.stdin.readline().strip()
word=sys.stdin.readline().strip()

# re.compile()
num=0
for i in range(len(word)):
    num=max(num,len(re.findall(word,doc[i:])))
print(num)