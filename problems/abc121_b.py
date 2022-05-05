N, M, C = map(int, input().split())
B = list(map(int, input().split()))

num = 0
for _ in range(N):
    A = list(map(int, input().split()))
    solve = (sum([A[i] * B[i] for i in range(M)]) + C) > 0
    if solve:
        num += 1

print(num)
