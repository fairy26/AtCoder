# TLE
# binary-searchしないといけないっぽい！

N = int(input())
As = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    [L, R, X] = list(map(int, input().split()))
    count = 0
    for a in As[L - 1 : R]:
        if a == X:
            count += 1
    print(count)
