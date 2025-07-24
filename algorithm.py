from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n, m, v = map(int, stdin.readline().split())

board = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, stdin.readline().split())

    board[x].append(y)
    board[y].append(x)

for i in range(1, n + 1):
    board[i].sort()


def DFS(idx):
    print(idx, end=" ")

    for i in board[idx]:
        if not visit[i]:
            visit[i] = True
            DFS(i)


def BFS(idx):
    que = deque()

    visit[idx] = True
    que.append(idx)

    while que:
        current = que.popleft()

        print(current, end=" ")

        for i in board[current]:
            if not visit[i]:
                visit[i] = True
                que.append(i)


visit[v] = True
DFS(v)
print()

visit = [False for _ in range(n + 1)]

BFS(v)
print()
