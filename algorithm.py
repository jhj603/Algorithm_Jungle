from sys import stdin
import heapq

stdin = open("input.txt", "r")

n = int(stdin.readline())

next_num = [[] for _ in range(n)]
counts = [0 for _ in range(n)]

for i in range(n):
    temp = stdin.readline().strip()

    for j in range(n):
        if "1" == temp[j]:
            next_num[j].append(i)
            counts[i] += 1

pq = []

for i in range(n):
    if not counts[i]:
        heapq.heappush(pq, -i)

res = [0] * n
cur_count = n

while pq:
    cur = -heapq.heappop(pq)

    res[cur] = cur_count
    cur_count -= 1

    for i in next_num[cur]:
        counts[i] -= 1

        if not counts[i]:
            heapq.heappush(pq, -i)

if 0 < cur_count:
    print(-1)
else:
    print(*res)
