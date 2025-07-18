from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

stack = []
res = []

for _ in range(n):
    inputs = list(stdin.readline().split())

    if "push" == inputs[0]:
        stack.append(int(inputs[1]))
    elif "pop" == inputs[0]:
        res.append(-1 if not stack else stack.pop())
    elif "size" == inputs[0]:
        res.append(len(stack))
    elif "empty" == inputs[0]:
        res.append(1 if not stack else 0)
    elif "top" == inputs[0]:
        res.append(-1 if not stack else stack[-1])

for i in res:
    print(i)
