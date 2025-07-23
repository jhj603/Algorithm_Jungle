from sys import stdin
import heapq

stdin = open("input.txt", "r")

n = int(stdin.readline())

end_diameter = []

for _ in range(n):
    x, r = map(int, stdin.readline().split())

    right = x + r

    end_diameter.append((right, r * 2))

end_diameter.sort()

pq = []
count = 1

for i in range(n):
    cur_end, cur_dia = end_diameter[i]
    cur_start = cur_end - cur_dia

    can_fill = False
    fill_point = cur_end

    while pq:
        e, d = heapq.heappop(pq)
        e = -e

        if e <= cur_start:
            heapq.heappush(pq, (-e, d))
            break
        if e != fill_point and cur_start <= (e - d):
            continue
        if cur_start <= (e - d):
            fill_point = e - d
        if fill_point == cur_start:
            can_fill = True

    count += 1

    if can_fill:
        count += 1

    heapq.heappush(pq, (-cur_end, cur_dia))

print(count)
