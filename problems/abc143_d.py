#  解法1　2分探索を自分で実装
# N = int(input())
# L = sorted(list(map(int, input().split())))


# def is_ok(a, b, c):
#     return L[a] + L[b] > L[c]


# cnt = 0
# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#         # 以下, 2分探索
#         l_idx = j
#         r_idx = N
#         while abs(l_idx - r_idx) > 1:
#             mid_idx = (l_idx + r_idx) // 2
#             if is_ok(i, j, mid_idx):
#                 l_idx = mid_idx
#             else:
#                 r_idx = mid_idx
#         cnt += l_idx - j

# print(cnt)

#  解法2 bisectによる二分探索
import bisect

N = int(input())
L = sorted(list(map(int, input().split())))

cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        min_idx = bisect.bisect_left(L, L[i] + L[j])
        cnt += min_idx - (j + 1)

print(cnt)
