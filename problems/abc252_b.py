N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
max = max(A)
max_indices = []
for i in range(N):
    if A[i] == max:
        max_indices.append(i + 1)

yes = False
for idx in max_indices:
    if idx in B:
        yes = True
        break

print("Yes" if yes else "No")
