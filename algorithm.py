from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n, m = map(int, stdin.readline().split())

# BFS 풀이
light_array = [[] for _ in range(n)]
heavy_array = [[] for _ in range(n)]

for _ in range(m):
    h, l = map(int, stdin.readline().split())

    h -= 1
    l -= 1

    light_array[h].append(l)
    heavy_array[l].append(h)


def bfs(array, visit, idx):
    que = deque()

    count = 0

    visit[idx] = True
    for j in array[idx]:
        if not visit[j]:
            visit[j] = True
            que.append(j)

    while que:
        current = que.popleft()

        count += 1

        for j in array[current]:
            if not visit[j]:
                visit[j] = True
                que.append(j)

    return count


result = 0
mid = (n // 2) + 1
for i in range(n):
    light = heavy = 0

    if light_array[i]:
        visit = [False] * n
        light = bfs(light_array, visit, i)

    if heavy_array[i]:
        visit = [False] * n
        heavy = bfs(heavy_array, visit, i)

    if (light >= mid) or (heavy >= mid):
        result += 1

print(result)

# 플로이드 워셜 풀이
# floyd = [[0 for _ in range(n)] for _ in range(n)]

# for _ in range(m):
#     h, l = map(int, stdin.readline().split())

#     h -= 1
#     l -= 1

#     floyd[h][l] = 1
#     floyd[l][h] = -1

# for k in range(n):
#     for i in range(n):
#         for j in range(i + 1, n):
#             if floyd[i][k] and (floyd[i][k] == floyd[k][j]):
#                 floyd[i][j] = floyd[i][k]
#                 floyd[j][i] = -floyd[i][k]

# count = 0

# for i in range(n):
#     plus_sum = minus_sum = 0

#     for j in range(n):
#         if 1 == floyd[i][j]:
#             plus_sum += 1
#         elif -1 == floyd[i][j]:
#             minus_sum += 1

#     mid = (n // 2) + 1
#     if plus_sum >= mid or minus_sum >= mid:
#         count += 1

# print(count)
