from sys import stdin

stdin = open('input.txt', 'r')

Array = list(stdin.readline().strip().split())

A = int(Array[0][::-1])
B = int(Array[1][::-1])

if (A > B):
    print(A)
else:
    print(B)
