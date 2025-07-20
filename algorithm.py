from sys import stdin
from collections import deque

stdin = open('input.txt', 'r')

n = int(stdin.readline())

queue = deque()

for i in range(1, n + 1):
    queue.append(i)

while 1 < len(queue):
    queue.popleft()

    queue.append(queue.popleft())

print(queue[0])
