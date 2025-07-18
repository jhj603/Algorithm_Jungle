from sys import stdin

stdin = open("input.txt", "r")

t = int(stdin.readline())

res = []

for _ in range(t):
    is_vps = True
    count = 0
    for i in stdin.readline().strip():
        if "(" == i:
            count += 1
        elif ")" == i:
            if not count:
                is_vps = False
                break
            else:
                count -= 1

    if is_vps and not count:
        res.append("YES")
    else:
        res.append("NO")

for i in res:
    print(i)
