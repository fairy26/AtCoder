N = int(input())

ans = "1"
for i in range(1, N):
    ans = f"{ans} {i+1} {ans}"

print(ans)
