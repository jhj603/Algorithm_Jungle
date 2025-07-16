from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

m = 0
array = list(map(int, stdin.readline().split()))
visit = [False] * len(array)


def solve(count, list):
    global m

    if n == count:
        sum = 0

        for i in range(len(list) - 1):
            sum += abs(list[i] - list[i + 1])

        m = max(m, sum)

        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            list.append(array[i])

            solve(count + 1, list)

            list.pop()
            visit[i] = False


solve(0, [])

print(m)


# N = int(stdin.readline())

# inputs = list(map(int, stdin.readline().split()))

# visit = [False] * N
# result_list = []
# result = 0


# def dfs(current_list):
#     global result

#     if N == len(current_list):
#         current_sum = 0
#         for i in range(N - 1):
#             current_sum += abs(current_list[i] - current_list[i + 1])
#         result = max(result, current_sum)
#         return

#     for i in range(N):
#         if not visit[i]:
#             visit[i] = True
#             current_list.append(inputs[i])
#             dfs(current_list)
#             current_list.pop()
#             visit[i] = False


# dfs([])

# print(result)
