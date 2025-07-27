from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n = int(stdin.readline())

roads = [[] for _ in range(n)]
reverse_roads = [[] for _ in range(n)]
counts = [0] * n
times = [0] * n
visit = [False] * n
long_roads = 0

m = int(stdin.readline())

for _ in range(m):
    start, to, time = map(int, stdin.readline().split())

    start -= 1
    to -= 1

    roads[start].append((to, time))
    reverse_roads[to].append((start, time))
    counts[to] += 1

start_point, end_point = map(int, stdin.readline().split())

start_point -= 1
end_point -= 1

que = deque()
que.append(start_point)

while que:
    cur = que.popleft()

    for i in roads[cur]:
        counts[i[0]] -= 1

        times[i[0]] = max(times[i[0]], times[cur] + i[1])

        if not counts[i[0]]:
            que.append(i[0])


print(times[end_point])

que.append(end_point)

while que:
    cur = que.popleft()

    for i in reverse_roads[cur]:
        if times[cur] == times[i[0]] + i[1]:
            long_roads += 1

            if not visit[i[0]]:
                visit[i[0]] = True
                que.append(i[0])

print(long_roads)
