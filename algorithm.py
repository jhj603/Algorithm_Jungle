from sys import stdin

#stdin = open('input.txt', 'r')

Array = list(stdin.readline().strip().split(' '))

Count = 0
for Str in Array:
    if "" != Str:
        Count += 1

print(Count)
