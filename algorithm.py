from sys import stdin

stdin = open("input.txt", "r")

n, r, c = map(int, stdin.readline().split())


def FindZ(num, x, y):
    count = 0

    if num:
        half = 2 ** (num - 1)

        if r < (x + half) and c < (y + half):
            count += FindZ(num - 1, x, y)
        elif r < (x + half) and c >= (y + half):
            count += (half**2) + FindZ(num - 1, x, y + half)
        elif r >= (x + half) and c < (y + half):
            count += 2 * (half**2) + FindZ(num - 1, x + half, y)
        else:
            count += 3 * (half**2) + FindZ(num - 1, x + half, y + half)

    return count


print(FindZ(n, 0, 0))

# # def DFS(num, x, y):
# #     if 0 == num:
# #         return 0

# #     ori_x, ori_y = x, y

# #     x //= 2
# #     y //= 2

# #     Min = DFS(num - 1, x, y) * 4

# #     Min += (ori_x - (x * 2)) * 2 + (ori_y - (y * 2))


# #     return Min
