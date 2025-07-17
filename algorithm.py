from sys import stdin

stdin = open("input.txt", "r")

# 이분 탐색 풀이 - 이분 탐색을 이용만 해서 푸는 문제
n = int(stdin.readline())

a = list(map(int, stdin.readline().split()))

lis = []


def binary_search(list, find):
    idx = len(list)

    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2

        if list[mid] >= find:
            idx = mid
            right = mid - 1
        else:
            left = mid + 1

    return idx


for i in a:
    if not lis or (lis[-1] < i):
        lis.append(i)
    else:
        lis[binary_search(lis, i)] = i


print(len(lis))

# DP 풀이
# n = int(stdin.readline())

# a = list(map(int, stdin.readline().split()))

# DP = [1 for _ in range(n)]  # 모든 원소는 길이 1짜리의 부분 수열이 될 수 있다.

# for i in range(n):
#     for j in range(i):
#         if a[j] < a[i]:
#             DP[i] = max(DP[i], DP[j] + 1)

# print(max(DP))
