# A - T-shirt

a, b, c, x = map(int, input().split())

p = 0.0

if x <= a:
    p = 1.0
elif x <= b:
    p = c / (b - a)

print(f"{p:.12f}")
