from sys import stdin

Max = 0
idx = -1

for i in range(9):
    N = int(stdin.readline().split()[0])

    if (Max < N):
        Max = N
        idx = i

print(Max)
print(idx + 1)