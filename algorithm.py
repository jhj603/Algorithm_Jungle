from sys import stdin

stdin = open("input.txt", "r")

m, n, l = map(int, stdin.readline().split())

shoot_pos = list(map(int, stdin.readline().split()))

animal_pos = []

for _ in range(n):
    animal_pos.append(tuple(map(int, stdin.readline().split())))

shoot_pos.sort()

count = 0


def binary_search(points, min_x):
    min_idx = len(points) - 1

    left = 0
    right = len(points) - 1

    while left <= right:
        mid = (left + right) // 2

        if min_x <= points[mid]:
            min_idx = mid
            right = mid - 1
        else:
            left = mid + 1

    return min_idx


for animal in animal_pos:
    if l < animal[1]:
        continue

    min_x = animal[0] - (l - animal[1])
    max_x = animal[0] + (l - animal[1])

    idx = binary_search(shoot_pos, min_x)

    if (min_x <= shoot_pos[idx]) and (max_x >= shoot_pos[idx]):
        count += 1


print(count)
