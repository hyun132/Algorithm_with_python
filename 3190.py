import sys
from collections import deque

#배열로 푸는게 훨씬 빠름.
if __name__ == '__main__':
    timeCount = 0
    mapSize = int(sys.stdin.readline().strip())
    numOfApples = int(sys.stdin.readline().strip())
    applePositions = []
    for _ in range(numOfApples):
        applePositions.append(tuple(map(int, sys.stdin.readline().split(' '))))

    control = int(sys.stdin.readline().strip())
    controls = []
    for _ in range(control):
        controls.append(sys.stdin.readline().strip().split(' '))

    controls.append(['100', 'x'])
    snake = deque()
    snake.append((1, 1))
    lastTime = 1
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    direction = 0
    for time, newdirection in controls:
        for timeCount in range(lastTime, int(time) + 1):
            newHead = (snake[0][0] + dirs[direction][0], snake[0][1] + dirs[direction][1])
            if 0 < newHead[0] <= mapSize and 0 < newHead[1] <= mapSize and newHead not in snake:
                if newHead in applePositions:
                    applePositions.remove(newHead)
                else:
                    snake.pop()
                snake.appendleft(newHead)
            else:
                print(timeCount)
                exit()
        if newdirection == 'L':
            direction = (direction + 1) % 4
        elif newdirection == 'D':
            direction = (direction + 4 - 1) % 4
        lastTime = int(time) + 1
