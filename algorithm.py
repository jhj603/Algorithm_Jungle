from sys import stdin
import math

stdin = open('input.txt', 'r')

A, B, V = map(int, stdin.readline().strip().split())

Count = 1
D = math.ceil((V - A) / (A - B))

print(Count + D)