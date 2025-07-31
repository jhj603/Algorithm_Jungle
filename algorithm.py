from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

if 1 == n:
    print(1)
elif 2 == n:
    print(2)
else:
    a = 1
    b = 2

    for i in range(3, n + 1):
        a, b = b, (a + b) % 15746

    print(b)

# i - 2 번째 친구들에게 00을 붙이고 i - 1번째 친구들에게 1을 붙이기 때문에 점화식이 피보나치와 동일하다
# DP = [0 for _ in range(max(3, n + 1))]

# DP[0] = 0
# DP[1] = 1
# DP[2] = 2

# for i in range(3, n + 1):
#     DP[i] = (DP[i - 1] + DP[i - 2]) % 15746

# print(DP[n])
