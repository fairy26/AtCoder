N = int(input())
p = sorted([int(input()) for _ in range(N)])
p[-1] //= 2
print(sum(p))
