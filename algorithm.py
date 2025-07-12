from sys import stdin

stdin = open('input.txt', 'r')

N = int(stdin.readline())
Array = [int(stdin.readline()) for _ in range(N)]

def Quick(List, start, end):
    
