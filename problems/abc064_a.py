# A - RGB Cards
r, g, b = map(int, input().split())
ok = (r * 100 + g * 10 + b) % 4 == 0
print("YES" if ok else "NO")
