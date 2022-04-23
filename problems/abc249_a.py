a, b, c, d, e, f, x = map(int, input().split())

takahashi = b * (a * (x // (a + c)) + min(a, x % (a + c)))
aoki = e * (d * (x // (d + f)) + min(d, x % (d + f)))

if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")
