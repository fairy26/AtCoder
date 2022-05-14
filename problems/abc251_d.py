#  解法1 (LTE) -- 2022-05-14
# from itertools import combinations


# def find_combination(A, comb_num, w):
#     for cmb in combinations(A, comb_num):
#         if sum(cmb) == w:
#             return True
#     return False


# W = int(input())

# A = set({1})
# for w in range(1, W + 1):
#     if find_combination(A, 2, w):
#         continue
#     if find_combination(A, 3, w):
#         continue
#     A.add(w)


# print(len(A))
# print(*A)

# 解法2 (WA) -- 公式解答のヒントを読んでから
# W = int(input())
# ans = [10 ** 6]
# i = 0
# for i in range(6):
#     ans += [(num + 1) * (10 ** i) for num in range(10)]

# print(len(ans))
# print(*ans)

# 解法3 -- 公式解答
W = int(input())

ans = []
for i in range(1, 100):
    for j in range(3):
        ans += [i * (100 ** j)]

print(len(ans))
print(*ans)
