from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n, m = map(int, stdin.readline().split())

relations = [[] for _ in range(n)]
counts = [0 for _ in range(n)]

for _ in range(m):
    t, s = map(int, stdin.readline().split())

    t -= 1
    s -= 1

    relations[t].append(s)
    counts[s] += 1

res = []
que = deque()

for i in range(n):
    if not counts[i]:
        que.append(i)

while que:
    cur = que.popleft()

    res.append(cur + 1)

    for j in relations[cur]:
        counts[j] -= 1

        if not counts[j]:
            que.append(j)

print(*res, sep=" ")
