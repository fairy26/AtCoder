R, C = map(int, input().split())
A = []
for _ in range(2):
    A.append(list(map(int, input().split())))
print(A[R - 1][C - 1])
