from sys import stdin
import heapq

stdin = open("input.txt", "r")

# 정렬 사용 풀이
n = int(stdin.readline())

meetings = []

count = 0
last_end = 0

for _ in range(n):
    start, end = map(int, stdin.readline().split())

    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    if last_end <= meetings[i][0]:
        count += 1
        last_end = meetings[i][1]

print(count)

# 우선순위 큐 사용 풀이
# n = int(stdin.readline())

# count = 0
# last_end = 0

# pq = []

# for _ in range(n):
#     start, end = map(int, stdin.readline().split())
#     heapq.heappush(pq, (end, start))

# while pq:
#     cur_end, cur_start = heapq.heappop(pq)

#     if cur_start >= last_end:
#         count += 1
#         last_end = cur_end

# print(count)
