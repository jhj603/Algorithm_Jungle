from sys import stdin
import heapq

stdin = open("input.txt", "r")

n, k = map(int, stdin.readline().split())

coins = []
visit = [float("inf")] * (k + 1)

for _ in range(n):
    coins.append(int(stdin.readline()))

coins = sorted(list(set(coins)))
n = len(coins)

pq = []

visit[0] = 0
heapq.heappush(pq, (0, 0))

while pq:
    cur_count, cur_sum = heapq.heappop(pq)

    if cur_count > visit[cur_sum]:
        continue

    for i in range(n):
        temp = cur_sum + coins[i]
        if (k >= temp) and (visit[temp] > cur_count + 1):
            visit[temp] = cur_count + 1
            heapq.heappush(pq, (visit[temp], temp))

if float("inf") == visit[k]:
    visit[k] = -1

print(visit[k])
