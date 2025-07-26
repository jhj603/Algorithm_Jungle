from sys import stdin
from collections import deque
import heapq

stdin = open("input.txt", "r")

n = int(stdin.readline())

track = [[] for _ in range(n)]

m = int(stdin.readline())

for _ in range(m):
    start, to, cost = map(int, stdin.readline().split())

    track[start - 1].append((to - 1, cost))

start_point, end_point = map(int, stdin.readline().split())

start_point -= 1
end_point -= 1

# 다익스트라 풀이
pq = []
cost = [float("inf")] * n

cost[start_point] = 0
heapq.heappush(pq, (0, start_point))

while pq:
    cur_cost, current = heapq.heappop(pq)

    if cur_cost > cost[current]:
        continue

    for i in track[current]:
        if cost[i[0]] > cur_cost + i[1]:
            cost[i[0]] = cur_cost + i[1]
            heapq.heappush(pq, (cur_cost + i[1], i[0]))

print(cost[end_point])

# BFS 풀이
# que = deque()
# visit = [float("inf")] * n

# visit[start_point] = 0
# que.append((start_point, 0))

# while que:
#     current, sum = que.popleft()

#     if sum > visit[current]:
#         continue

#     for i in track[current]:
#         if visit[i[0]] > sum + i[1]:
#             visit[i[0]] = sum + i[1]
#             que.append((i[0], visit[i[0]]))

# print(visit[end_point])
