from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n = int(stdin.readline())

tree = [[] for _ in range(n)]
visit = [False] * n
parents = [0] * n

for i in range(1, n):
    u, v = map(int, stdin.readline().split())

    u -= 1
    v -= 1

    tree[u].append(v)
    tree[v].append(u)


def bfs(start):
    que = deque([start])
    visit[start] = True

    while que:
        current = que.popleft()

        for i in tree[current]:
            if not visit[i]:
                visit[i] = True
                parents[i] = current + 1
                que.append(i)


bfs(0)

for i in range(1, n):
    print(parents[i])
