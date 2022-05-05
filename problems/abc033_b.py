#  解法1
N = int(input())

S = []
P = []
for i in range(N):
    s, p = input().split()
    S.append(s)
    P.append(int(p))

p_mean = sum(P) / 2

for i in range(N):
    if P[i] > p_mean:
        print(S[i])
        exit()

print("atcoder")

#  解法2: 実行時エラーになった
# N = int(input())

# SP = {}
# for i in range(N):
#     s, p = input().split()
#     SP[s] = int(p)
# SP_ = sorted(SP.items(), key=lambda x: x[1])

# print(SP_[-1][0] if SP_[-1][1] > sum(SP.values()) / 2 else "atcoder")
