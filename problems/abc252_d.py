#  解法1 - TLE
# from itertools import combinations
# from collections import Counter


# N = int(input())
# A = list(map(int, input().split()))

# cnt = Counter(A)  # O(N)
# sum = 0
# for idx in combinations(cnt.keys(), 3):  # O(N!)
#     sum += cnt[idx[0]] * cnt[idx[1]] * cnt[idx[2]]

# print(sum)
