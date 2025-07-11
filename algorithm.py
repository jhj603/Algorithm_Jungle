from sys import stdin

C = int(stdin.readline().strip())

for i in range(C):
    Sum = 0
    Count = 0

    Input = list(map(int, stdin.readline().split()))

    for j in range(1, Input[0] + 1):
        Sum += Input[j]
    
    Avg = Sum // Input[0]

    for j in range(1, Input[0] + 1):
        if Avg < Input[j]:
            Count += 1
    
    print(f"{round(Count/Input[0]*100, 3)}%")