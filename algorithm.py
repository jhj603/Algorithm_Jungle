from sys import stdin
import math

stdin = open('input.txt', 'r')

def is_Prime(num):
    if 1 == num:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if 0 == num % i:
            return False
        
    return True

stdin.readline()

Array = list(map(int, stdin.readline().strip().split()))

Count = 0

for a in Array:
    if is_Prime(a):
        Count += 1

print(Count)