from sys import stdin

stdin = open("input.txt", "r")

# DP 풀이
n = int(stdin.readline())

a = list(map(int, stdin.readline().split()))

DP = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))

# 이분 탐색 풀이 - 이분 탐색을 이용만 해서 푸는 문제
# n = int(stdin.readline())

# a = list(map(int, stdin.readline().split()))

# lis = []


# def binary_search(list, find):
#     idx = len(list)

#     left = 0
#     right = len(list) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if list[mid] >= find:
#             idx = mid
#             right = mid - 1
#         else:
#             left = mid + 1

#     return idx


# for i in a:
#     if not lis or (lis[-1] < i):
#         lis.append(i)
#     else:
#         lis[binary_search(lis, i)] = i


# print(len(lis))
