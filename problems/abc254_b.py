n = int(input())

A = [[1] * n for _ in range(n)]

for i in range(n):
    for j in range(1, i):
        A[i][j] = A[i - 1][j - 1] + A[i - 1][j]

    print(*A[i][: i + 1])
