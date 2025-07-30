from sys import stdin
from collections import deque
import heapq

stdin = open("input.txt", "r")

n = int(stdin.readline())

# DFS + 메모이제이션 어렵지만 40ms로 제일 빠르다. pypy에서도 100ms의 벽을 뚫었다.
need_parts = [[] for _ in range(n)]
total = [{} for _ in range(n)]

m = int(stdin.readline())

for _ in range(m):
    x, y, k = map(int, stdin.readline().split())

    x -= 1
    y -= 1

    need_parts[x].append((y, k))


def dfs(idx):
    if total[idx]:
        return total[idx]

    if not need_parts[idx]:
        total[idx][idx] = 1
        return total[idx]

    for i in need_parts[idx]:
        temp_dict = dfs(i[0])

        for j in temp_dict:
            if j in total[idx]:
                total[idx][j] += temp_dict[j] * i[1]
            else:
                total[idx][j] = temp_dict[j] * i[1]

    return total[idx]


dfs(n - 1)

for key, value in sorted(total[n - 1].items()):
    print(f"{key + 1} {value}")


# DP 풀이 그러나 딕셔너리 풀이와 시간적 차이는 없고 메모리는 조금 더 먹으며 코드 길이가 짧다는 이점 밖에 없다..
# 아니었다! 이상하게 pypy보다 python3가 더 빠르다! 시현님 코드와 동일한 56ms가 나온다!
# 딕셔너리 풀이가 4ms 더 느리다!
# need_parts = [[] for _ in range(n)]
# counts = [0 for _ in range(n)]
# total = [[0 for _ in range(n)] for _ in range(n)]

# m = int(stdin.readline())

# for _ in range(m):
#     x, y, k = map(int, stdin.readline().split())

#     x -= 1
#     y -= 1

#     need_parts[y].append((x, k))
#     counts[x] += 1

# que = deque()

# for i in range(n):
#     if not counts[i]:
#         que.append(i)
#         total[i][i] = 1

# while que:
#     cur = que.pop()

#     for i in need_parts[cur]:
#         for j in range(n):
#             total[i[0]][j] += total[cur][j] * i[1]

#         counts[i[0]] -= 1

#         if not counts[i[0]]:
#             que.append(i[0])

# for i in range(n):
#     if total[n - 1][i]:
#         print(f"{i + 1} {total[n - 1][i]}")


# 딕셔너리로 푼 방법 - 비효율적인 것 같다.
# need_parts = [[] for _ in range(n)]
# counts = [0 for _ in range(n)]
# total = [{} for _ in range(n)]

# m = int(stdin.readline())

# for _ in range(m):
#     x, y, k = map(int, stdin.readline().split())

#     x -= 1
#     y -= 1

#     need_parts[y].append((x, k))
#     counts[x] += 1

# que = deque()

# for i in range(n):
#     if not counts[i]:
#         que.append(i)
#         total[i][i] = 1

# while que:
#     cur = que.popleft()

#     for i in need_parts[cur]:
#         counts[i[0]] -= 1

#         for j in total[cur]:
#             if j in total[i[0]]:
#                 total[i[0]][j] += total[cur][j] * i[1]
#             else:
#                 total[i[0]][j] = total[cur][j] * i[1]

#         if not counts[i[0]]:
#             que.append(i[0])

# for key, value in sorted(total[n - 1].items()):
#     print(f"{key + 1} {value}")
