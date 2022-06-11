X, A, D, N = map(int, input().split())
first, last = A, (A + (N - 1) * D)
min_S, max_S = min(first, last), max(first, last)

if X < min_S:
    print(abs(min_S - X))
elif X > max_S:
    print(abs(X - max_S))
else:
    if D != 0:
        num = (X - min_S) % abs(D)
        print(min(num, abs(D) - num))
    else:
        print(abs(X - A))
