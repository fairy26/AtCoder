N, K = map(int, input().split())
S = [input() for _ in range(N)]

chars = {}
for i in range(N):
    for s in S[i]:
        if s not in chars:
            chars[s] = 1
        else:
            chars[s] += 1

# 動的計画法で解けそうだけどわからん！！
# dp = [[0] * K for _ in range(N)]

# for j in range(K):
#     if j >= len(S[0]):
#         dp[0][j] =  len(S[0])
# before = [s for s in S[0]]
# for i in range(1, N):
#     for j in range(K):
#         not_choice = dp[i-1][j]
#         if j < len(S[i]):
#             dp[i][j] = not_choice
#         else:
#             pass
