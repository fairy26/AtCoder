N, M = map(int, input().split())
likes = [0] * M
for _ in range(N):
    _, *A = map(int, input().split())
    for idx in A:
        likes[idx - 1] += 1

print(sum([num == N for num in likes]))
