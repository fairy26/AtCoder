N, Y = list(map(int, input().split()))

for i in range(N + 1):
    for j in range(N + 1):
        k = N - i - j
        if k >= 0:
            if i * 10000 + j * 5000 + k * 1000 == Y:
                print(i, j, k)
                exit()

print(-1, -1, -1)
