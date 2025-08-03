from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

# 최대 속도를 유추해 DP 테이블을 만들어 푸는 풀이
n, m = map(int, stdin.readline().split())

rocks = [True] * (n + 1)

for _ in range(m):
    rocks[int(stdin.readline())] = False

DP = [[float("inf") for _ in range(n + 1)] for _ in range(int((2 * n) ** 0.5) + 1)]

DP[0][1] = 0

que = deque()

que.append((0, 1))

while que:
    speed, cur = que.popleft()

    for next_speed in range(speed - 1, speed + 2):
        next_pos = cur + next_speed

        if (
            (cur < next_pos <= n)
            and rocks[next_pos]
            and (DP[next_speed][next_pos] > DP[speed][cur] + 1)
        ):
            DP[next_speed][next_pos] = DP[speed][cur] + 1
            que.append((next_speed, next_pos))

result = float("inf")

for i in DP:
    result = min(result, i[n])

if float("inf") == result:
    print(-1)
else:
    print(result)

# 힌트만으로 최대 속도를 유추할 수 없다 가정하고 딕셔너리를 이용해서 푼 풀이
# n, m = map(int, stdin.readline().split())

# rocks = [True] * (n + 1)

# for _ in range(m):
#     rocks[int(stdin.readline())] = False

# DP = {0: [float("inf") for _ in range(n + 1)]}

# DP[0][1] = 0

# que = deque()

# que.append((0, 1))

# while que:
#     speed, cur = que.popleft()

#     for next in range(speed - 1, speed + 2):
#         if not next in DP:
#             DP[next] = [float("inf") for _ in range(n + 1)]

#         next_pos = cur + next
#         if (
#             (cur < next_pos <= n)
#             and (DP[next][next_pos] > DP[speed][cur] + 1)
#             and rocks[next_pos]
#         ):
#             DP[next][next_pos] = DP[speed][cur] + 1
#             que.append((next, next_pos))

# result = float("inf")

# for table in DP.values():
#     result = min(result, table[n])

# if float("inf") == result:
#     print(-1)
# else:
#     print(result)
