import sys
from collections import deque

sys.setrecursionlimit(10**5)
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

tree = [[] for _ in range(n)]
visit = [False] * n
parents = [0] * n

for i in range(1, n):
    u, v = map(int, sys.stdin.readline().split())

    u -= 1
    v -= 1

    tree[u].append(v)
    tree[v].append(u)


# DFS 풀이
def dfs(start):
    for i in tree[start]:
        if not visit[i]:
            visit[i] = True
            parents[i] = start + 1
            dfs(i)


visit[0] = True
dfs(0)

# BFS 풀이
# def bfs(start):
#     que = deque([start])
#     visit[start] = True

#     while que:
#         current = que.popleft()

#         for i in tree[current]:
#             if not visit[i]:
#                 visit[i] = True
#                 parents[i] = current + 1
#                 que.append(i)


# bfs(0)

for i in range(1, n):
    print(parents[i])
