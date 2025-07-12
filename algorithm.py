from sys import stdin

stdin = open("input.txt", "r")

N = int(stdin.readline())

Array = [int(stdin.readline()) for _ in range(N)]


def Quick(List, start, end):
    if start < end:
        pivot_index = part(List, start, end)

        Quick(List, start, pivot_index - 1)
        Quick(List, pivot_index + 1, end)


def part(List, start, end):
    pivot = List[end]
    i = start - 1

    for j in range(start, end):
        if pivot >= List[j]:
            i += 1
            List[i], List[j] = List[j], List[i]

    List[i + 1], List[end] = List[end], List[i + 1]
    return i + 1


Quick(Array, 0, N - 1)

for num in Array:
    print(num)
