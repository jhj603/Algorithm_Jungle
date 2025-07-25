import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

tree = [[] for _ in range(n)]
visit = [False] * n

a = sys.stdin.readline().strip()

for i in range(1, n):
    u, v = map(int, sys.stdin.readline().split())

    u -= 1
    v -= 1

    tree[u].append(v)
    tree[v].append(u)


def find_pre(start):
    total_count = 0

    for i in tree[start]:
        if "1" == a[i]:
            total_count += 1
        elif not visit[i] and ("0" == a[i]):
            visit[i] = True
            total_count += find_pre(i)

    return total_count


count = 0
temp = 0
for i in range(n):
    if "0" == a[i]:
        if not visit[i]:
            visit[i] = True
            temp = find_pre(i)
            count += temp * (temp - 1)
    else:
        for node in tree[i]:
            if "1" == a[node]:
                count += 1

print(count)
