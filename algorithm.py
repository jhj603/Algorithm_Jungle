import sys

sys.setrecursionlimit(10**5)
sys.stdin = open("input.txt", "r")

nodes = []

while True:
    line_input = sys.stdin.readline().strip()

    if not line_input:
        break

    nodes.append(int(line_input))

result = []


def subtree(root, end):
    if root >= end:
        return

    high_idx = end

    for i in range(root + 1, end):
        if nodes[root] < nodes[i]:
            high_idx = i
            break

    subtree(root + 1, high_idx)
    subtree(high_idx, end)
    result.append(nodes[root])


subtree(0, len(nodes))

print(*result, sep="\n")
