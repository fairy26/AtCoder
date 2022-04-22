# B - Maximum Difference

N = int(input())
As = list(map(int, input().split()))

max_ = 1
min_ = 10 ** 9
for i in range(N):
    if As[i] > max_:
        max_ = As[i]
    if As[i] < min_:
        min_ = As[i]

print(max_ - min_)
