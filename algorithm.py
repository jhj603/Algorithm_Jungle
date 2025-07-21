from sys import stdin
import heapq

stdin = open('input.txt', 'r')

pq = []

n = int(stdin.readline())

ans = 0

for _ in range(n):
    heapq.heappush(pq, int(stdin.readline()))

while 1 < len(pq):
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)

    ans += (a + b)
    heapq.heappush(pq, a + b)

print(ans)
