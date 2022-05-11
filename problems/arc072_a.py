N = int(input())
A = list(map(int, input().split()))

cnt = 0
total = 0
# 正負正負...
for i in range(N):
    total += A[i]
    if i % 2 != 0:  # 奇数 = 正
        if total <= 0:
            cnt += abs(total) + 1
            total = 1
    else:
        if total >= 0:
            cnt += abs(total) + 1
            total = -1

# 負正負正...
cnt_ = cnt
cnt = 0
total = 0
for i in range(N):
    total += A[i]
    if i % 2 == 0:  # 偶数 = 正
        if total <= 0:
            cnt += abs(total) + 1
            total = 1
    else:
        if total >= 0:
            cnt += abs(total) + 1
            total = -1

print(min(cnt, cnt_))
