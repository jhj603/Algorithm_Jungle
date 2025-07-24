from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n, m = map(int, stdin.readline().split())

# BFS 풀이
board = [[] for _ in range(n)]
visit = [False] * n

count = 0

for _ in range(m):
    u, v = map(int, stdin.readline().split())

    u -= 1
    v -= 1

    board[u].append(v)
    board[v].append(u)

que = deque()


def bfs():
    while que:
        current = que.pop()

        for i in board[current]:
            if not visit[i]:
                visit[i] = True
                que.append(i)


for i in range(n):
    if not visit[i]:
        visit[i] = True
        que.append(i)
        count += 1
        bfs()

print(count)

# Union-Find 풀이
# parents = [i for i in range(n + 1)]
# depth = [0 for _ in range(n + 1)]


# def find_parent(idx):
#     if idx == parents[idx]:
#         return idx

#     parents[idx] = find_parent(parents[idx])

#     return parents[idx]


# for _ in range(m):
#     u, v = map(int, stdin.readline().split())

#     u = find_parent(u)
#     v = find_parent(v)

#     if u != v:
#         if depth[u] < depth[v]:
#             parents[u] = v
#         elif depth[u] > depth[v]:
#             parents[v] = u
#         else:
#             parents[v] = u
#             depth[u] += 1

# set_result = set()

# for i in range(1, n + 1):
#     set_result.add(find_parent(parents[i]))

# print(len(set_result))
