from sys import stdin

stdin = open("input.txt", "r")

# 이분 탐색 풀이 - 이분 탐색을 이용만 해서 푸는 문제


# DP 풀이
# n = int(stdin.readline())

# a = list(map(int, stdin.readline().split()))

# DP = [1 for _ in range(n)]  # 모든 원소는 길이 1짜리의 부분 수열이 될 수 있다.

# for i in range(n):
#     for j in range(i):
#         if a[j] < a[i]:
#             DP[i] = max(DP[i], DP[j] + 1)

# print(max(DP))
