from sys import stdin
import heapq

stdin = open("input.txt", "r")

N = int(stdin.readline())

heap = []

for _ in range(N):
    heapq.heappush(heap, int(stdin.readline()))

for _ in range(N):
    print(heapq.heappop(heap))
