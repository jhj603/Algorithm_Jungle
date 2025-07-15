import sys

sys.setrecursionlimit(10**6)
stdin = open("input.txt", "r")

num = [0 for _ in range(100001)]
num[0] = 1

for i in range(1, 100001):
    num[i] = (num[i - 1] * 2) % 1000000

n = int(stdin.readline())

a, b, c = map(int, stdin.readline().split())

pos = [0 for _ in range(n)]

for i in range(3):
    input_list = list(map(int, stdin.readline().split()))

    for input in input_list:
        pos[input - 1] = i

        if n == input:
            target_rod = i

print(target_rod + 1)

Sum = 0


def hanoi(cur, to):
    if 0 == cur:
        return

    global Sum, num, pos

    now = pos[cur - 1]

    for i in range(3):
        if (now != i) and (to != i):
            sub = i
            break

    if now == to:
        hanoi(cur - 1, to)
    else:
        Sum = (Sum + num[cur - 1]) % 1000000
        hanoi(cur - 1, sub)


hanoi(n, target_rod)

print(Sum)
