from sys import stdin

stdin = open("input.txt", "r")

N = int(stdin.readline())

min_cost = float("inf")
cost_array = [list(map(int, stdin.readline().split())) for _ in range(N)]
visit = [False] * N


def dfs(cur, sum, count):
    global min_cost

    if (N - 1) == count:
        if cost_array[cur][0]:
            min_cost = min(min_cost, sum + cost_array[cur][0])
        return

    for i in range(N):
        if not visit[i] and cost_array[cur][i]:
            visit[i] = True
            dfs(i, sum + cost_array[cur][i], count + 1)
            visit[i] = False


visit[0] = True
dfs(0, 0, 0)
print(min_cost)
