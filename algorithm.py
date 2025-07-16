from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())
q = list(map(int, stdin.readline().split()))

col = [False] * n

ld = [False] * (n * 2 - 1)
rd = [False] * (n * 2 - 1)

for i in range(n):
    if 0 != q[i]:
        col_idx = q[i] - 1
        col[col_idx] = ld[i + col_idx] = rd[(n - 1) - (i - col_idx)] = True


def queen(cur_idx):
    if n == cur_idx:
        print(*q)
        return True

    if 0 != q[cur_idx]:
        return queen(cur_idx + 1)

    for i in range(n):
        if not col[i] and not ld[cur_idx + i] and not rd[(n - 1) - (cur_idx - i)]:
            col[i] = ld[cur_idx + i] = rd[(n - 1) - (cur_idx - i)] = True
            q[cur_idx] = i + 1

            if queen(cur_idx + 1):
                return True

            q[cur_idx] = 0
            col[i] = ld[cur_idx + i] = rd[(n - 1) - (cur_idx - i)] = False

    return False


if not queen(0):
    print(-1)
