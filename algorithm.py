from sys import stdin

stdin = open("input.txt", "r")

# 기수 정렬 + 맨버-마이어스 알고리즘 + 카사이 알고리즘이 합쳐진 기적의 문제
# 간단해보이지만 자그마치 3가지 알고리즘이 섞인 콤비네이션 문제

def make_suffix_array(s):
    n = len(s)
    sa = list(range(n))

    rank = [ord(c) for c in s]

    k = 1

    while k < n:
        # pairs = [(rank[i], rank[i + k] if i + k < n else -1, i) for i in range(n)]
        pairs = []

        for i in range(n):
            if i + k < n:
                pairs.append((rank[i], rank[i + k], i))
            else:
                pairs.append((rank[i], -1, i))

        pairs.sort()

        # sa.sort(key=lambda i: rank[i + k] if i + k < n else -1)
        # sa.sort(key=lambda i: rank[i])

        new_rank = [0] * n
        # new_rank[pairs[0][2]] = 0
        new_rank[sa[0]] = 0

        for i in range(1, n):
            a = pairs[i - 1][:2]
            b = pairs[i][:2]

            if pairs[i - 1][:2] == pairs[i][:2]:
                new_rank[pairs[i][2]] = new_rank[pairs[i - 1][2]]
            else:
                new_rank[pairs[i][2]] = new_rank[pairs[i - 1][2]] + 1

        # for i in range(1, n):
        #     is_same = (rank[sa[i]] == rank[sa[i - 1]]) and (
        #         (rank[sa[i] + k] if sa[i] + k < n else -1)
        #         == (rank[sa[i - 1] + k] if sa[i - 1] + k < n else -1)
        #     )

        #     if is_same:
        #         new_rank[sa[i]] = new_rank[sa[i - 1]]
        #     else:
        #         new_rank[sa[i]] = new_rank[sa[i - 1]] + 1

        rank = new_rank
        k *= 2

    return [p[2] for p in pairs]
    # return sa


def make_lcp_array(s, sa):
    n = len(s)
    lcp = [0] * n
    rank = [0] * n

    for i in range(n):
        rank[sa[i]] = i

    h = 0

    for i in range(n):
        if rank[i] == n - 1:
            h = 0
            continue

        j = sa[rank[i] + 1]

        if h > 0:
            h -= 1

        while (i + h < n) and (j + h < n) and (s[i + h] == s[j + h]):
            h += 1

        lcp[rank[i]] = h

    return lcp


# a = stdin.readline().strip()
# b = stdin.readline().strip()

# s = a + chr(0) + b + chr(1)

# sa = make_suffix_array(s)
# lcp_array = make_lcp_array(s, sa)

# len_a = len(a)

# max_lcp = 0
# start_index = -1

# for i in range(len(lcp_array)):
#     if lcp_array[i] > max_lcp:
#         is_from_a = sa[i] < len_a
#         is_from_b = sa[i + 1] < len_a

#         if is_from_a != is_from_b:
#             max_lcp = lcp_array[i]

#             start_index = min(sa[i], sa[i + 1])

s = "banana"
sa = make_suffix_array(s)
lcp_array = make_lcp_array(s, sa)
print(sa)
print(lcp_array)

# print(max_lcp)
# print(s[start_index : start_index + max_lcp])
