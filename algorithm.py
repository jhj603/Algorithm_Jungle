from sys import stdin
import heapq

stdin = open('input.txt', 'r')

pq = []

n = int(stdin.readline())

result = []

for _ in range(n):
    x = int(stdin.readline())

    if 0 == x:
        if pq:
            result.append(-heapq.heappop(pq))
        else:
            result.append(0)
    else:
        heapq.heappush(pq, -x)

for i in result:
    print(i)
