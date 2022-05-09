[A, B, K] = list(map(int, input().split()))

i = 0
while (K ** i) * A < B:
    i += 1

print(i)
