#  解法1 - 愚直にcountして差を求める
# N = int(input())
# s = [input() for _ in range(N)]
# M = int(input())
# t = [input() for _ in range(M)]

# cnt = {}
# for i in range(N):
#     if s[i] not in cnt:
#         cnt[s[i]] = 1
#     else:
#         cnt[s[i]] += 1

# for j in range(M):
#     if t[j] in cnt:
#         cnt[t[j]] -= 1

# print(max(max(cnt.values()), 0))

#  解法2 - setを用いて候補を列挙する
N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]
words = list(set(s))
print(max(0, max([s.count(w) - t.count(w) for w in words])))
