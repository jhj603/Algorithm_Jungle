from sys import stdin

stdin = open("input.txt", "r")

N = int(stdin.readline())

Array = [0 for _ in range(10001)]

for _ in range(N):
    Array[int(stdin.readline())] += 1

for i in range(10001):
    for _ in range(Array[i]):
        print(i)
