from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n, m = map(int, stdin.readline().split())

board = []

for _ in range(n):
    row = list(map(int, stdin.readline().split()))

    board.append(row)

add = [(1, 0), (-1, 0), (0, 1), (0, -1)]

year = 0

que = deque()


def counting_ice(board, visit, n, m):
    count = 0

    for i in range(n):
        for j in range(m):
            if 0 != board[i][j] and not visit[i][j]:
                count += 1
                visit[i][j] = True

                que.append((i, j))

                while que:
                    x, y = que.popleft()

                    for k in range(4):
                        tempx = x + add[k][0]
                        tempy = y + add[k][1]

                        if not visit[tempx][tempy] and board[tempx][tempy]:
                            visit[tempx][tempy] = True
                            que.append((tempx, tempy))

    return count


while True:
    year += 1

    next_board = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if 0 != board[i][j]:
                count = 0

                for k in range(4):
                    tempx = i + add[k][0]
                    tempy = j + add[k][1]

                    if 0 == board[tempx][tempy]:
                        count += 1

                    next_board[i][j] = max(0, board[i][j] - count)

    board = next_board

    visit = [[False for _ in range(m)] for _ in range(n)]
    count = counting_ice(board, visit, n, m)

    if not count:
        year = 0
        break
    elif 1 < count:
        break

print(year)
