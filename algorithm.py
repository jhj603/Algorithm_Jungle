from sys import stdin

stdin = open("input.txt", "r")

N, r, c = map(int, stdin.readline().split())


# def DFS(num, x, y):
#     if 0 == num:
#         return 0

#     ori_x, ori_y = x, y

#     x //= 2
#     y //= 2

#     Min = DFS(num - 1, x, y) * 4

#     Min += (ori_x - (x * 2)) * 2 + (ori_y - (y * 2))


#     return Min
def DFS(num, x, y):
    if num == 0:
        return 0

    half = 2 ** (num - 1)

    if r < x + half and c < y + half:
        return DFS(num - 1, x, y)

    elif r < x + half and c >= y + half:
        return half**2 + DFS(num - 1, x, y + half)

    elif r >= x + half and c < y + half:
        return 2 * (half**2) + DFS(num - 1, x + half, y)

    else:
        return 3 * (half**2) + DFS(num - 1, x + half, y + half)


print(DFS(N, 0, 0))
