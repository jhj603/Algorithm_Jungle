from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

r, c = map(int, stdin.readline().split())

board = []

water_time = [[float("inf")] * c for _ in range(r)]
dochi_time = [[float("inf")] * c for _ in range(r)]

water_que = deque()
dochi_que = deque()

goal_x = goal_y = -1

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(r):
    temp = list(stdin.readline().strip())

    for j in range(c):
        if "D" == temp[j]:
            goal_x, goal_y = i, j
        elif "S" == temp[j]:
            dochi_que.append((i, j))
            dochi_time[i][j] = 0
        elif "*" == temp[j]:
            water_que.append((i, j))
            water_time[i][j] = 0

    board.append(temp)

while water_que:
    x, y = water_que.popleft()

    for i in range(4):
        tempx = x + directions[i][0]
        tempy = y + directions[i][1]

        if (
            (0 <= tempx < r)
            and (0 <= tempy < c)
            and ("X" != board[tempx][tempy])
            and ("D" != board[tempx][tempy])
            and (float("inf") == water_time[tempx][tempy])
        ):
            water_time[tempx][tempy] = water_time[x][y] + 1
            water_que.append((tempx, tempy))

while dochi_que:
    x, y = dochi_que.popleft()

    if (goal_x == x) and (goal_y == y):
        break

    for i in range(4):
        tempx = x + directions[i][0]
        tempy = y + directions[i][1]

        if (
            (0 <= tempx < r)
            and (0 <= tempy < c)
            and ("X" != board[tempx][tempy])
            and (float("inf") == dochi_time[tempx][tempy])
        ):
            if water_time[tempx][tempy] > dochi_time[x][y] + 1:
                dochi_time[tempx][tempy] = dochi_time[x][y] + 1
                dochi_que.append((tempx, tempy))

time = dochi_time[goal_x][goal_y]

if float("inf") == time:
    time = "KAKTUS"

print(time)
