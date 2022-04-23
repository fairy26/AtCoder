# C - Digits in Multiplication
import math


def F(a, b):
    num = max(a, b)
    i = 0
    while num > 0:
        num //= 10
        i += 1
    return i


N = int(input())
min_f = 10
for i in range(int(math.sqrt(N))):
    a = i + 1
    if N % a != 0:
        continue

    b = N // a
    min_f = min(min_f, F(a, b))

print(min_f)
