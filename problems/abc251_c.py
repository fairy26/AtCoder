N = int(input())
S = []
T = []
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))

originals = {}
max = 0
max_idx = -1
for i in range(N):
    if S[i] not in originals:
        originals[S[i]] = T[i]
        if T[i] > max:
            max = T[i]
            max_idx = i

print(max_idx + 1)
