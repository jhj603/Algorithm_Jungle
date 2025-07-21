import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

board = [[0 for _ in range(n)] for _ in range(n)]
queue = deque([(0, 0)])
board[0][0] = 2

cur_dir = 0
cur_time = 0

add = [(0, 1), (-1, 0), (0, -1), (1, 0)]

k = int(sys.stdin.readline())

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())

    board[x - 1][y - 1] = 1

l = int(sys.stdin.readline())

change_directions = {}

for _ in range(l):
    time, change_dir = sys.stdin.readline().split()
    time = int(time)

    change_directions[time] = change_dir

while True:
    tempx = queue[-1][0] + add[cur_dir][0]
    tempy = queue[-1][1] + add[cur_dir][1]

    cur_time += 1
    
    if ((0 <= tempx) and (0 <= tempy) and (n > tempx) and (n > tempy)):
        if 2 == board[tempx][tempy]:
            break
            
        queue.append((tempx, tempy))

        if not board[tempx][tempy]:
            tail_x, tail_y = queue.popleft()
            board[tail_x][tail_y] = 0
        
        board[tempx][tempy] = 2

        if cur_time in change_directions:
            if 'L' == change_directions[cur_time]:
                cur_dir = (cur_dir + 1) % 4
            else:
                cur_dir = (cur_dir + 3) % 4 
    else:
        break       

print(cur_time)
        
