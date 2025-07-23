from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

dots = []

for _ in range(n):
    x, y = map(int, stdin.readline().split())

    dots.append((x, y))

dots.sort()


def recursion_dots(left, right):
    min_dist = float("inf")

    if 3 > right - left:
        for i in range(left, right - 1):
            for j in range(i + 1, right):
                min_dist = min(
                    min_dist,
                    (dots[j][0] - dots[i][0]) ** 2 + (dots[j][1] - dots[i][1]) ** 2,
                )

        return min_dist

    mid = (left + right) // 2

    min_result = min(recursion_dots(left, mid), recursion_dots(mid, right))

    mid_array = []

    for i in range(left, right):
        if min_result >= (dots[mid][0] - dots[i][0]) ** 2:
            mid_array.append(dots[i])

    mid_array.sort(key=lambda x: x[1])

    for i in range(len(mid_array) - 1):
        for j in range(i + 1, len(mid_array)):
            if min_result <= (mid_array[i][1] - mid_array[j][1]) ** 2:
                break

            min_result = min(
                min_result,
                (mid_array[i][0] - mid_array[j][0]) ** 2
                + (mid_array[i][1] - mid_array[j][1]) ** 2,
            )

    return min_result


print(recursion_dots(0, len(dots)))
