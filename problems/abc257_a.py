N, X = map(int, input().split())
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(abc[(X + N - 1) // N - 1])
