L, H = map(int, input().split())
N = int(input())
A = [int(input()) for _ in range(N)]

for a in A:
    print(max(0, L - a) if a <= H else -1)
