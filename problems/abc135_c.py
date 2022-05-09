N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(N):
    here = min(A[i], B[i])
    nxt = min(A[i + 1], B[i] - here)
    A[i + 1] -= nxt
    cnt += here + nxt

print(cnt)
