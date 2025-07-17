from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

array = list(map(int, stdin.readline().split()))

array.sort()

m = int(stdin.readline())

find = list(map(int, stdin.readline().split()))

for find_num in find:
    left = 0
    right = n - 1

    found = False

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == find_num:
            found = True
            break

        if array[mid] > find_num:
            right = mid - 1
        else:
            left = mid + 1

    if found:
        print(1)
    else:
        print(0)
