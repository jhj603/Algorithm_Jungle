Input = input().split(' ')

x = int(Input[0])
y = int(Input[1])
w = int(Input[2])
h = int(Input[3])

print(min(min(x, abs(w - x)), min(y, abs(h - y))))
