K = int(input())
A, B = map(int, input().split())


def ten(num, K):
    i, ret = 0, 0
    while num > 0:
        ret += (num % 10) * (K ** i)
        num //= 10
        i += 1
    return ret


print(ten(A, K) * ten(B, K))
