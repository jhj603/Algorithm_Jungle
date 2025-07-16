from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

col = [False for _ in range(n)]

ld = [False for _ in range(n * 2 - 1)]
rd = [False for _ in range(n * 2 - 1)]

q = list(map(int, stdin.readline().split()))

cur_count = 0

for i in range(n):
    if 0 != q[i]:
        col[q[i] - 1] = ld[i + q[i] - 1] = rd[(n - 1) - (i - q[i] + 1)] = True
        cur_count += 1

can_place = False


def dfs(cur_idx):
    global can_place

    if n == cur_idx:
        can_place = True

        for i in q:
            print(i, end=" ")
        print()

        return
    else:
        if 0 != q[cur_idx]:
            dfs(cur_idx + 1)
        else:
            for i in range(n):
                if (
                    not can_place
                    and not col[i]
                    and not ld[cur_idx + i]
                    and not rd[(n - 1) - (cur_idx - i)]
                ):
                    col[i] = ld[cur_idx + i] = rd[(n - 1) - (cur_idx - i)] = True
                    q[cur_idx] = i + 1
                    dfs(cur_idx + 1)
                    q[cur_idx] = 0
                    col[i] = ld[cur_idx + i] = rd[(n - 1) - (cur_idx - i)] = False


dfs(0)

if not can_place:
    print(-1)
