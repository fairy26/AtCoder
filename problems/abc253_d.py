import math


def lcm(a: int, b: int) -> int:
    y = a * b // math.gcd(a, b)
    return y


def sum_1_n(n: int) -> int:
    ret = (n * (n + 1)) // 2
    return ret


N, A, B = map(int, input().split())
n = sum_1_n(N)
a = A * sum_1_n(N // A)
b = B * sum_1_n(N // B)
lcm_AB = lcm(A, B)
ab = lcm_AB * sum_1_n(N // lcm_AB)
print(n - a - b + ab)
