from sys import stdin

stdin = open("input.txt", "r")

N = int(stdin.readline())


def hanoi_count(num):
    return (2**N) - 1


def hanoi_order(num, start, end, sub):
    if 1 == num:
        print(f"{start} {end}")
        return

    hanoi_order(num - 1, start, sub, end)
    print(f"{start} {end}")
    hanoi_order(num - 1, sub, end, start)


print(hanoi_count(N))

if 21 > N:
    hanoi_order(N, 1, 3, 2)
