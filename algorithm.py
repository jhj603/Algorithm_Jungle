from sys import stdin

Count = [0] * 10

A = int(stdin.readline().strip())
B = int(stdin.readline().strip())
C = int(stdin.readline().strip())

for word in str(A * B * C):
    Count[int(word)] += 1

for c in Count:
    print(c)