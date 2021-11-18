import sys

repeat = int(sys.stdin.readline().strip())

for _ in range(repeat):
    func = sys.stdin.readline().strip().replace('RR', '')
    right = int(sys.stdin.readline().strip())
    arr = list(sys.stdin.readline().strip()[1:-1].split(','))
    if func.count('D') > right:
        print("error")
    elif func.count('D') == right:
        print([])
    else:
        left = 0
        right -= 1
        is_reversed = False
        for char in func:
            if char == 'D':
                if is_reversed:
                    right -= 1
                else:
                    left += 1
            elif char == 'R':
                is_reversed = not is_reversed

        answer = arr[left:right + 1]
        if is_reversed:
            answer.reverse()
        print("[" + ",".join(answer) + "]")
