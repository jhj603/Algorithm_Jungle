from sys import stdin

stdin = open("input.txt", "r")

k = int(stdin.readline())


def dfs(start, g, v, side):
    bipartite = True

    for i in g[start]:
        if side == v[i]:
            bipartite = False
            break
        elif 0 == v[i]:
            v[i] = side * -1
            bipartite = dfs(i, g, v, side * -1)

    return bipartite


for _ in range(k):
    v, e = map(int, stdin.readline().split())

    graph = [[] for _ in range(v)]
    visit = [0] * v
    is_bipartite = True

    for _ in range(e):
        a, b = map(int, stdin.readline().split())

        a -= 1
        b -= 1

        graph[a].append(b)
        graph[b].append(a)

    for i in range(v):
        if 0 == visit[i] and is_bipartite:
            visit[i] = 1
            is_bipartite = dfs(i, graph, visit, 1)

    if is_bipartite:
        print("YES")
    else:
        print("NO")
