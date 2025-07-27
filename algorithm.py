from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n = int(stdin.readline())

need_parts = [[] for _ in range(n)]
counts = [0 for _ in range(n)]
total = [{} for _ in range(n)]

m = int(stdin.readline())

for _ in range(m):
    x, y, k = map(int, stdin.readline().split())

    x -= 1
    y -= 1

    need_parts[y].append((x, k))
    counts[x] += 1

que = deque()

for i in range(n):
    if not counts[i]:
        que.append(i)
        total[i][i] = 1

while que:
    cur = que.popleft()

    for i in need_parts[cur]:
        counts[i[0]] -= 1

        for j in total[cur]:
            if j in total[i[0]]:
                total[i[0]][j] += total[cur][j] * i[1]
            else:
                total[i[0]][j] = total[cur][j] * i[1]

        if not counts[i[0]]:
            que.append(i[0])

for key, value in sorted(total[n - 1].items()):
    print(f"{key + 1} {value}")
