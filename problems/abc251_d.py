#  解法1 (LTE) -- 2022-05-14
from itertools import combinations


def find_combination(A, comb_num, w):
    for cmb in combinations(A, comb_num):
        if sum(cmb) == w:
            return True
    return False


W = int(input())

A = set({1})
for w in range(1, W + 1):
    if find_combination(A, 2, w):
        continue
    if find_combination(A, 3, w):
        continue
    A.add(w)


print(len(A))
print(*A)
