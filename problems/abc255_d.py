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
N, Q = map(int, input().split())
A = tuple(map(int, input().split()))

for i in range(Q):  # O(2x10^5)
    X = int(input())
    ans = 0
    print(ans)
