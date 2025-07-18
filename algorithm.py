from sys import stdin
import sys

stdin = open("input.txt", "r")

res = []


def divide_square(array, left, right):
    if left == right:
        return array[left]

    elif 1 == (right - left):
        if array[right] < array[left]:
            return max(2 * array[right], array[left])
        else:
            return max(2 * array[left], array[right])

    mid = (left + right) // 2

    left_area = divide_square(array, left, mid)
    right_area = divide_square(array, mid + 1, right)

    next_left = mid - 1
    next_right = mid + 1

    mid_area = now_height = array[mid]

    while left <= next_left and right >= next_right:
        if array[next_left] < array[next_right]:
            if array[next_right] < now_height:
                now_height = array[next_right]

            mid_area = max(mid_area, now_height * (next_right - next_left))
            next_right += 1
        else:
            if array[next_left] < now_height:
                now_height = array[next_left]

            mid_area = max(mid_area, now_height * (next_right - next_left))
            next_left -= 1

    while left <= next_left:
        if array[next_left] < now_height:
            now_height = array[next_left]

        mid_area = max(mid_area, now_height * (next_right - next_left))
        next_left -= 1
    while right >= next_right:
        if array[next_right] < now_height:
            now_height = array[next_right]

        mid_area = max(mid_area, now_height * (next_right - next_left))
        next_right += 1

    return max(left_area, right_area, mid_area)


while True:
    inputs = list(map(int, stdin.readline().split()))

    if not inputs[0]:
        break

    n = inputs[0]

    res.append(divide_square(inputs, 1, n))

for i in res:
    print(i)
