from sys import stdin
import math

stdin = open("input.txt", "r")

n = int(stdin.readline())

paper = [list(map(int, stdin.readline().split())) for _ in range(n)]

count = int(math.log(n, 2))

white = blue = 0

add = [(0, 0), (0, 1), (1, 0), (1, 1)]


def cut_paper(num, x, y):
    global white, blue

    white_count = blue_count = 0

    for i in range(2**num):
        for j in range(2**num):
            if not paper[x + i][y + j]:
                white_count += 1
            else:
                blue_count += 1

    if white_count:
        if not blue_count:
            white += 1
        else:
            for a in add:
                cut_paper(
                    num - 1, x + a[0] * (2 ** (num - 1)), y + a[1] * (2 ** (num - 1))
                )
    else:
        blue += 1


cut_paper(count, 0, 0)

print(white)
print(blue)
