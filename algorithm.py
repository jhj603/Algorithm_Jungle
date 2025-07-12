from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

array = []

for i in range(n):
    array.append(stdin.readline().strip())

result = sorted(list(set(array)), key=lambda x: (len(x), x))

for word in result:
    print(word)
