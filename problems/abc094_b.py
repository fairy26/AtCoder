N, M, X = map(int, input().split())

A = [0] * (N + 1)
for i in list(map(int, input().split())):
    A[i] = 1

print(min(sum(A[X + 1 :]), sum(A[:X])))
