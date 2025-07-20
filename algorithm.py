from sys import stdin
from collections import deque

stdin = open('input.txt', 'r')

n = int(stdin.readline())

queue = deque()

result = []

for _ in range(n):
    inputs = list(stdin.readline().split())

    if 'push' == inputs[0]:
        queue.append(int(inputs[1]))
    elif 'pop' == inputs[0]:
        if not queue:
            result.append(-1)
        else:
            result.append(queue.popleft())
    elif 'size' == inputs[0]:
        result.append(len(queue))
    elif 'empty' == inputs[0]:
        if queue:
            result.append(0)
        else:
            result.append(1)
    elif 'front' == inputs[0]:
        if not queue:
            result.append(-1)
        else:
            result.append(queue[0])
    elif 'back' == inputs[0]:
        if not queue:
            result.append(-1)
        else:
            result.append(queue[-1])

for i in result:
    print(i)    
