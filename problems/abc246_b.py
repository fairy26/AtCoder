import math

A, B = map(float, input().split())

unit = 1 / math.sqrt(A ** 2 + B ** 2)
print(f"{A*unit:.012f} {B*unit:.012f}")
