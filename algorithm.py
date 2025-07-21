from sys import stdin
import heapq

stdin = open('input.txt', 'r')

n = int(stdin.readline())

max_que = []
min_que = []

for _ in range(n):
    k = int(stdin.readline())

    if len(max_que) == len(min_que):
        heapq.heappush(max_que, -k)
    else:
        heapq.heappush(min_que, k)

    if max_que and min_que and -max_que[0] > min_que[0]:
        temp = -heapq.heappop(max_que)
        heapq.heappush(max_que, -heapq.heappop(min_que))
        heapq.heappush(min_que, temp)
    
    print(-max_que[0])
