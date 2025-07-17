from sys import stdin

stdin = open("input.txt", "r")

n, m = map(int, stdin.readline().split())

trees = list(map(int, stdin.readline().split()))

left = 0
right = max(trees)

result = 0

while left <= right:
    mid = (left + right) // 2

    sum = 0

    for i in range(0, n):
        sum += max(0, trees[i] - mid)

    if m <= sum:
        result = max(result, mid)
        left = mid + 1
    else:
        right = mid - 1

print(result)
