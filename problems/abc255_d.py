#  解法1: TLE
# import numpy as np


# N, Q =  map(int, input().split())
# A = tuple(map(int, input().split()))

# for i in range(Q): # O(2x10^5)
#     np_A = np.array(A)
#     X = int(input())
#     ans = np.sum(np_A[np_A > X] - X) + np.sum(X - np_A[np_A <= X])
#     print(ans)

#  解法2
import bisect

N, Q = map(int, input().split())  # [1, 2x10^5]
A = tuple(map(int, input().split()))

A = sorted(A)
sum_A = A[:]  # 累積和
for i in range(1, N):  # O(N)
    sum_A[i] += sum_A[i - 1]

for i in range(Q):  # O(N)
    X = int(input())
    k = bisect.bisect_left(A, X)  # O(logN)
    idx = k - 1
    if idx >= 0:
        ans = k * X - sum_A[idx] + (sum_A[-1] - sum_A[idx]) - (N - k) * X  # O(1)
    else:
        ans = sum_A[-1] - N * X  # O(1)
    print(ans)
