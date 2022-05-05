X, Y = map(int, input().split("."))

if 0 <= Y <= 2:
    print(f"{X}-")
elif 3 <= Y <= 6:
    print(X)
elif 7 <= Y <= 9:
    print(f"{X}+")
