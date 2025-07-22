from sys import stdin
from collections import deque

stdin = open('input.txt', 'r')

stack = deque()

n, k = map(int, stdin.readline().split())

cur_count = 0

for i in stdin.readline().strip():
    while stack and (cur_count < k) and (stack[-1] < i):
        stack.pop()
        cur_count += 1

    stack.append(i)

while cur_count < k:
    stack.pop()
    cur_count += 1

result = "".join(stack)

print(result)