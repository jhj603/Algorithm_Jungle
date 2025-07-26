from sys import stdin
import heapq

stdin = open("input.txt", "r")

n = int(stdin.readline())

board = []
cost = [[float("inf") for _ in range(n)] for _ in range(n)]

for _ in range(n):
    board.append([int(char) for char in stdin.readline().strip()])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

pq = []
cost[0][0] = 0
heapq.heappush(pq, (0, (0, 0)))

while pq:
    cur_cost, coords = heapq.heappop(pq)
    x, y = coords

    if cur_cost > cost[x][y]:
        continue

    for i in range(4):
        tempx = x + directions[i][0]
        tempy = y + directions[i][1]

        if 0 <= tempx < n and 0 <= tempy < n:
            cost_to_move = 1 - board[tempx][tempy]

            next_cost = cur_cost + cost_to_move
            if cost[tempx][tempy] > next_cost:
                cost[tempx][tempy] = next_cost
                heapq.heappush(pq, (cost[tempx][tempy], (tempx, tempy)))

print(cost[n - 1][n - 1])
