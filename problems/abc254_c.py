#  解法1: TLE
# n, k = map(int, input().split())
# A = list(map(int, input().split()))

# ok = True
# sorted_A = sorted(A)
# for i, a in enumerate(sorted_A):  # n
#     tmp = A[i::k]  # n
#     if a in tmp:  # n
#         idx = tmp.index(a) * k + i
#         A[i], A[idx] = A[idx], A[i]
#         continue
#     ok = False
#     break

# print("Yes" if ok else "No")

#  解法2
n, k = map(int, input().split())
A = list(map(int, input().split()))

B = []
for i in range(k):  # O(k)
    B.append(sorted(A[i::k]))  # O(n)
# ^-- O(k*n)

B_flatten = []
for i in range(n):  # O(n)
    B_flatten.append(B[i % k][i // k])  # O(1)
# ^-- O(n)

print("Yes" if sorted(A) == B_flatten else "No")
