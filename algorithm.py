import sys

sys.stdin = open("input.txt", "r")

v, e = map(int, sys.stdin.readline().split())

node_union = [i for i in range(v)]
depth = [0] * v

line_list = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    line_list.append([c, a - 1, b - 1])

line_list.sort()

result = 0


def find_parent(idx):
    if idx == node_union[idx]:
        return idx

    node_union[idx] = find_parent(node_union[idx])

    return node_union[idx]


for line in line_list:
    a = find_parent(line[1])
    b = find_parent(line[2])

    if a != b:
        if depth[a] < depth[b]:
            node_union[a] = b
        elif depth[a] > depth[b]:
            node_union[b] = a
        else:
            node_union[b] = a
            depth[a] += 1

        result += line[0]

print(result)
