from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

tree = {}

for _ in range(n):
    inputs = list(stdin.readline().split())

    tree[inputs[0]] = inputs[1:]


def preorder_tail(cur):
    result = []

    stack = [cur]

    while stack:
        cur_node = stack.pop()

        result.append(cur_node)

        if "." != tree[cur_node][1]:
            stack.append(tree[cur_node][1])
        if "." != tree[cur_node][0]:
            stack.append(tree[cur_node][0])

    return "".join(result)


def inorder_tail(cur):
    result = []
    stack = []

    current = cur

    while "." != current or stack:
        while "." != current:
            stack.append(current)
            current = tree[current][0]

        current = stack.pop()
        result.append(current)

        current = tree[current][1]

    return "".join(result)


def postorder_tail(cur):
    result = []
    stack = [cur]

    while stack:
        cur_node = stack.pop()

        result.append(cur_node)

        if "." != tree[cur_node][0]:
            stack.append(tree[cur_node][0])
        if "." != tree[cur_node][1]:
            stack.append(tree[cur_node][1])

    return "".join(reversed(result))


print(preorder_tail("A"))

print(inorder_tail("A"))

print(postorder_tail("A"))
