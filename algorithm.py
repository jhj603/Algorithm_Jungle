from sys import stdin

stdin = open("input.txt", "r")

# 앞에서부터 뒤로 가면서 수행하는 방식 - 추천 방식
input = stdin.readline().strip().split("-")

result = sum(map(int, input[0].split("+")))

for i in range(1, len(input)):
    temp = sum(map(int, input[i].split("+")))

    result -= temp

print(result)

# 뒤에서부터 앞으로 오면서 수행하는 방식
# input = stdin.readline().strip()

# is_meet_minus = False

# result = 0
# temp = 0
# last_idx = len(input)

# for i in range(len(input) - 1, -1, -1):
#     if "-" == input[i]:
#         result -= temp + int(input[i + 1 : last_idx])
#         temp = 0
#         last_idx = i
#     elif "+" == input[i]:
#         temp += int(input[i + 1 : last_idx])
#         last_idx = i

# result += temp + int(input[0:last_idx])

# print(result)
