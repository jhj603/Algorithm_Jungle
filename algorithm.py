from sys import stdin
from collections import deque

stdin = open("input.txt", "r")

n, k = map(int, stdin.readline().split())

order = list(map(int, stdin.readline().split()))

indices = [deque() for _ in range(k + 1)]

for i in range(k):
    indices[order[i]].append(i)

unplug_count = 0

plug = set()

for i in range(k):
    if n <= len(plug) and not order[i] in plug:
        max_count = 0
        max_idx = -1

        for item in plug:
            if not indices[item]:
                gap = float("inf")
            else:
                gap = indices[item][0] - i

            if max_count < gap:
                max_count = gap
                max_idx = item

        plug.discard(max_idx)

        unplug_count += 1

    plug.add(order[i])

    if indices[order[i]]:
        indices[order[i]].popleft()

print(unplug_count)
