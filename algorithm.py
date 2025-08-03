from sys import stdin

stdin = open("input.txt", "r")

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())

    test_result = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

    test_result.sort()

    count = 1
    last = test_result[0][1]

    for i in range(1, n):
        if test_result[i][1] > last:
            continue

        count += 1
        last = test_result[i][1]

    print(count)
