from sys import stdin

stdin = open("input.txt", "r")

stack = []

k = int(stdin.readline())

for _ in range(k):
    num = int(stdin.readline())

    if 0 == num:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
