from sys import stdin

Input = list(map(int, stdin.readline().split()))
N = Input[0]
X = Input[1]

A = list(map(int, stdin.readline().split()))

for a in A:
    if (X > a):
        print(a, end=" ")
print()