N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for next_i in L:
    now_i = next_i - 1
    if A[now_i] >= N:
        continue

    ok = True
    if next_i < K:
        ok = A[now_i] + 1 < A[next_i]
    if ok:
        A[now_i] += 1

print(*A)
