from sys import stdin

stdin = open("input.txt", "r")

n, c = map(int, stdin.readline().split())

array = [int(stdin.readline()) for _ in range(n)]

array.sort()

left = 1
right = array[-1] - array[0]

result = 0

while left <= right:
    mid = (left + right) // 2

    count = 1
    current = array[0] + mid

    for i in range(n):
        if array[i] >= current:
            count += 1
            current = array[i] + mid

    if c <= count:
        result = max(result, mid)
        left = mid + 1
    else:
        right = mid - 1

print(result)
