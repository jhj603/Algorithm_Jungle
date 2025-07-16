from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())


def hanoi(num, start, end, sub):
    result = []

    stack = [(num, start, end, sub)]

    while stack:
        cur_num, s, e, a = stack.pop()

        if 1 == cur_num:
            result.append((s, e))
        else:
            stack.append((cur_num - 1, a, e, s))
            stack.append((1, s, e, a))
            stack.append((cur_num - 1, s, a, e))

    return result


after_hanoi = hanoi(n, 1, 3, 2)

print(len(after_hanoi))
for start, end in after_hanoi:
    print(f"{start} {end}")
