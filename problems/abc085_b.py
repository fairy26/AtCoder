#  ABC085B - Kagami Mochi
#  解法1
# N = int(input())

# mochis = []
# X = 0
# for i in range(N):
#     mochis.append(int(input()))

# mochis.sort()

# ex = 0
# i = N - 1
# while i >= 0:
#     if ex != mochis[i]:
#         ex = mochis[i]
#     else:
#         mochis.pop(i)
#     i -= 1

# print(len(mochis))

#  解法2 - 2022/05/02
N = int(input())
d = [int(input()) for _ in range(N)]
print(len(set(d)))
