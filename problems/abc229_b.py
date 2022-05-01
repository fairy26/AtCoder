A, B = map(int, input().split())

ans = "Easy"

while min(A, B) > 0:
    num = (A % 10) + (B % 10)
    if num >= 10:
        ans = "Hard"
        break
    A //= 10
    B //= 10

print(ans)
