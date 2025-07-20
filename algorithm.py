from sys import stdin

stdin = open('input.txt', 'r')

inputs = stdin.readline()

stack = []

sum = 0

wrong = False

for i in inputs:
    if '(' == i or '[' == i:
        stack.append(i)
    elif ')' == i:
        if not stack or '[' == stack[-1]:
            wrong = True
            break

        temp = 0
        while stack and '(' != stack[-1]:
            if not isinstance(stack[-1], int):
                wrong = True
                break
            temp += stack.pop()
            
        if wrong:
            break
        
        if not stack or '(' != stack[-1]:
            wrong = True
            break

        stack.pop()
        stack.append(max(temp * 2, 2))
        
    elif ']' == i:
        if not stack or '(' == stack[-1]:
            wrong = True
            break

        temp = 0
        while stack and '[' != stack[-1]:
            if not isinstance(stack[-1], int):
                wrong = True
                break
            temp += stack.pop()
        
        if wrong:
            break

        if not stack or '[' != stack[-1]:
            wrong = True
            break
        
        stack.pop()
        stack.append(max(temp * 3, 3))
        
for i in stack:
    if not isinstance(i, int):
        wrong = True
        break

if not wrong:
    for i in stack:
        sum += i
else:
    sum = 0

print(sum)