from sys import stdin

stdin = open('input.txt', 'r')

def is_Hansu(num):
    if 100 > num:
        return True
    
    strTemp = str(num)
    Array = list(map(int, strTemp))

    if ((Array[1] - Array[0]) == (Array[2] - Array[1])):
        return True
    
    return False

Count = 0

N = int(stdin.readline())

for i in range(1, N + 1):
    if is_Hansu(i):
        Count += 1

print(Count)