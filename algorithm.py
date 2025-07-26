from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n, m = map(int, stdin.readline().split())

board = []
visit = [[-1 for _ in range(m)] for _ in range(n)]

add = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for _ in range(n):
    board.append(list(map(int, stdin.readline().strip())))

que = deque()

visit[0][0] = 1
que.append((0, 0))

while que:
    x, y = que.popleft()

    for i in range(4):
        tempx = x + add[i][0]
        tempy = y + add[i][1]

        if (
            (0 <= tempx)
            and (0 <= tempy)
            and (n > tempx)
            and (m > tempy)
            and board[tempx][tempy]
            and (-1 == visit[tempx][tempy])
        ):
            visit[tempx][tempy] = visit[x][y] + 1
            que.append((tempx, tempy))

print(visit[n - 1][m - 1])
