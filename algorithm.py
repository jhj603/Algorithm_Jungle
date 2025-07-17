from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

array = list(map(int, stdin.readline().split()))

array.sort()

result = 10**8

left = ans_l = ans_r = 0
right = n - 1

while left <= right:
    temp_sum = array[left] + array[right]

    if result > abs(temp_sum):
        result = temp_sum
        ans_l = array[left]
        ans_r = array[right]

    if 0 < temp_sum:
        right -= 1
    else:
        left += 1


print(f"{ans_l} {ans_r}")
