from sys import stdin

stdin = open('input.txt', 'r')

n = int(stdin.readline())

circles = []

stack = []

def get_interval(element):
    return element[1] - element[0]

for _ in range(n):
    x, r = map(int, stdin.readline().split())

    left = x - r
    right = x + r

    circles.append((left, right))

circles.sort(key=get_interval, reverse=True)

for i in range(n):
    if not stack:
        stack.append(circles[i])

a = 10