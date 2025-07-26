from sys import stdin
from collections import deque
import heapq

stdin = open("input.txt", "r")

n, m, k, x = map(int, stdin.readline().split())

x -= 1

# 다익스트라 풀이 - 왜 bfs보다 더 느린지 모르겠다.
array = [[] for _ in range(n)]
dist = [float("inf") for _ in range(n)]

for _ in range(m):
    start, to = map(int, stdin.readline().split())

    start -= 1
    to -= 1

    array[start].append(to)

pq = []
dist[x] = 0
heapq.heappush(pq, (0, x))

while pq:
    sum, current = heapq.heappop(pq)

    if sum > dist[current]:
        continue

    for i in array[current]:
        if dist[i] > sum + 1:
            dist[i] = sum + 1
            heapq.heappush(pq, (sum + 1, i))

res = []
for i in range(n):
    if k == dist[i]:
        res.append(i + 1)

if not res:
    print(-1)
else:
    print(*res, sep="\n")

# BFS 풀이
# array = [[] for _ in range(n)]
# min_dist = [float("inf") for _ in range(n)]

# for _ in range(m):
#     start, to = map(int, stdin.readline().split())

#     start -= 1
#     to -= 1

#     array[start].append(to)

# que = deque()
# min_dist[x] = 0
# que.append((x, 0))

# while que:
#     current, sum = que.popleft()

#     for j in array[current]:
#         if min_dist[j] > sum + 1:
#             min_dist[j] = sum + 1
#             que.append((j, sum + 1))

# res = []
# for i in range(n):
#     if k == min_dist[i]:
#         res.append(i + 1)

# if not res:
#     print(-1)
# else:
#     print(*res, sep="\n")


# 플로이드 워셜 풀이 - 되는 것 같긴 한데 메모리가 부족하다 메모리 터진다
# floyd = [[-1 for _ in range(n)] for _ in range(n)]

# for i in range(n):
#     floyd[i][i] = 0

# for _ in range(m):
#     start, to = map(int, stdin.readline().split())

#     start -= 1
#     to -= 1

#     floyd[start][to] = 1

# for l in range(n):
#     for i in range(n):
#         for j in range(i + 1, n):
#             if (-1 < floyd[i][l]) and (-1 < floyd[l][j]):
#                 if -1 == floyd[i][j]:
#                     floyd[i][j] = floyd[i][l] + floyd[l][j]
#                 else:
#                     floyd[i][j] = min(floyd[i][j], floyd[i][l] + floyd[l][j])

# res = []
# for i in range(n):
#     if k == floyd[x][i]:
#         res.append(i + 1)

# if not res:
#     print(-1)
# else:
#     print(*res, sep="\n")
