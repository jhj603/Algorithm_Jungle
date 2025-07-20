from sys import stdin

stdin = open('input.txt', 'r')

n = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))

res = []
stack = []

for i in range(n):
    while stack and towers[stack[-1]] <= towers[i]:
        stack.pop()

    if not stack:
        res.append(0)
    else:
        res.append(stack[-1] + 1)
    
    stack.append(i) 

print(*res)