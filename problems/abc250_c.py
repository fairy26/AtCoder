# 2022-05-08 TLE
N, Q = map(int, input().split())
X = [int(input()) for _ in range(Q)]

ball = list(range(1, N + 1))

for x in X:
    i = ball.index(x)
    j = i + 1 if i < N - 1 else i - 1
    ball[i], ball[j] = ball[j], ball[i]

print(*ball)
