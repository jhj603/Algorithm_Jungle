from sys import stdin
import heapq

stdin = open("input.txt", "r")

W, H = list(map(int, stdin.readline().split()))

wArray = []
hArray = []

heapq.heappush(hArray, H)
heapq.heappush(wArray, W)

N = int(stdin.readline())

for i in range(N):
    How, Where = list(map(int, stdin.readline().split()))

    if 0 == How:
        heapq.heappush(hArray, Where)
    else:
        heapq.heappush(wArray, Where)

MaxW = 0
pre = 0
while wArray:
    cur = heapq.heappop(wArray)
    MaxW = max(MaxW, cur - pre)
    pre = cur

MaxH = 0
pre = 0
while hArray:
    cur = heapq.heappop(hArray)
    MaxH = max(MaxH, cur - pre)
    pre = cur


print(MaxH * MaxW)
