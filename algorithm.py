from sys import stdin

T = int(stdin.readline().split()[0])

for i in range(T):
    Count = Sum = 0
    Input = stdin.readline()

    for word in Input:
        if 'O' == word:
            Count += 1
            Sum += Count
        else:
            Count = 0

    print(Sum)
