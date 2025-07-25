from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

a = list(map(int, stdin.readline().split()))

oper_count = list(map(int, stdin.readline().split()))

min_result = float("inf")
max_result = float("-inf")


def dfs(idx, sum):
    if n == idx:
        global min_result, max_result

        min_result = min(min_result, sum)
        max_result = max(max_result, sum)

        return

    for i in range(4):
        if oper_count[i]:
            oper_count[i] -= 1

            if 0 == i:
                dfs(idx + 1, sum + a[idx])
            elif 1 == i:
                dfs(idx + 1, sum - a[idx])
            elif 2 == i:
                dfs(idx + 1, sum * a[idx])
            else:
                if 0 > sum:
                    dfs(idx + 1, -(-sum // a[idx]))
                else:
                    dfs(idx + 1, sum // a[idx])

            oper_count[i] += 1


dfs(1, a[0])

print(max_result)
print(min_result)
