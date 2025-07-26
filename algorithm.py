from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

m, n, h = map(int, stdin.readline().split())

directions = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

tomatos = []

for _ in range(h):
    tomatos.append([list(map(int, stdin.readline().split())) for _ in range(n)])

que = deque()

unripe_tomatos = 0

for z in range(h):
    for x in range(n):
        for y in range(m):
            if 0 == tomatos[z][x][y]:
                unripe_tomatos += 1
            elif 1 == tomatos[z][x][y]:
                que.append((z, x, y))

while que:
    cur_z, cur_x, cur_y = que.popleft()

    for i in range(6):
        tempz = cur_z + directions[i][0]
        tempx = cur_x + directions[i][1]
        tempy = cur_y + directions[i][2]

        if (
            (0 <= tempz < h)
            and (0 <= tempx < n)
            and (0 <= tempy < m)
            and (0 == tomatos[tempz][tempx][tempy])
        ):
            tomatos[tempz][tempx][tempy] = tomatos[cur_z][cur_x][cur_y] + 1
            que.append([tempz, tempx, tempy])
            unripe_tomatos -= 1

if not unripe_tomatos:
    days = 0

    for i in range(h):
        for j in range(n):
            days = max(days, max(tomatos[i][j]))

    days -= 1
else:
    days = -1

print(days)
