from sys import stdin

stdin = open("input.txt", "r")

max_h = 0
count = 0
stack = []

n = int(stdin.readline())

for _ in range(n):
    stack.append(int(stdin.readline()))

for i in range(n - 1, -1, -1):
    if max_h < stack[i]:
        max_h = stack[i]
        count += 1

print(count)
