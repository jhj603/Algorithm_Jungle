from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n = int(stdin.readline())

coms = [[] for _ in range(n)]
visit = [False] * n

m = int(stdin.readline())

for _ in range(m):
    u, v = map(int, stdin.readline().split())

    u -= 1
    v -= 1

    coms[u].append(v)
    coms[v].append(u)


def bfs(start):
    que = deque([start])
    visit[start] = True

    count = 0

    while que:
        current = que.popleft()

        for i in coms[current]:
            if not visit[i]:
                visit[i] = True
                count += 1
                que.append(i)

    return count


print(bfs(0))
