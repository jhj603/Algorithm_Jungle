from sys import stdin

stdin = open("input.txt", "r")

array = [int(stdin.readline()) for _ in range(9)]

sum = sum(array)

found = False
for i in range(9):
    if found:
        break

    for j in range(i + 1, 9):
        if sum - (array[i] + array[j]) == 100:
            sub1 = array[i]
            sub2 = array[j]

            array.remove(sub1)
            array.remove(sub2)

            found = True
            break

array.sort()
for h in array:
    print(h)
