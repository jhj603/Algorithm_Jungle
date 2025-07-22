from sys import stdin
import heapq

stdin = open('input.txt', 'r')

n = int(stdin.readline())

lines = []
pq = []

max_count = 0

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    
    lines.append((min(x, y), max(x, y)))

lines.sort(key=lambda line: (line[1], line[0]))

d = int(stdin.readline())

for i in lines:
    start = i[1] - d

    if start > i[0]:
        continue
        
    heapq.heappush(pq, i)

    while pq and pq[0][0] < start:
        heapq.heappop(pq)

    max_count = max(max_count, len(pq))

print(max_count)