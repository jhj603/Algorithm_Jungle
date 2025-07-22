from sys import stdin

stdin = open('input.txt', 'r')

n, b = map(int, stdin.readline().split())

array = [list(map(int, stdin.readline().split())) for _ in range(n)]

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    result[i][i] = 1

def matrix_mul(left, right):
    mul_result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                mul_result[i][j] = (mul_result[i][j] + (left[i][k] * right[k][j])) % 1000

    return mul_result

while (b):
    if b % 2:
        result = matrix_mul(result, array)

    array = (matrix_mul(array, array))
    b //= 2

for i in range(n):
    for j in range(n):
        print(result[i][j], end=" ")
    print()