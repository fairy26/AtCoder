# B - Break Number
N = int(input())

count = {}
for i in range(N):
    n = i + 1
    key = str(n)
    count[key] = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            count[key] += 1
        else:
            break

print(max(count, key=count.get))
