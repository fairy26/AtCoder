# ABC086A - Product
a, b = map(int, input().split())
odd = (a * b) % 2
if odd:
    print("Odd")
else:
    print("Even")
