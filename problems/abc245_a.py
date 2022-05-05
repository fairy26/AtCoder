A, B, C, D = map(int, input().split())

ans = "Aoki"
if A < C or (A == C and B <= D):
    ans = "Takahashi"
print(ans)
