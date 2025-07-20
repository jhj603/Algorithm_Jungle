from sys import stdin
from collections import deque

stdin = open('input.txt', 'r')

n, k = map(int, stdin.readline().split())

queue = deque(range(1, n + 1))

result = []

while queue:
    queue.rotate(-(k - 1))

    result.append(queue.popleft())

print(f"<{', '.join(map(str, result))}>")