N, T = map(int, input().split())
ct = [map(int, input().split()) for _ in range(N)]

ans = 1010
for c, t in ct:
    if t <= T:
        ans = min(ans, c)

print(ans if ans != 1010 else "TLE")
