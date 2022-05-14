N, W = map(int, input().split())
A = list(map(int, input().split()))


def is_good(num):
    if num <= W:
        return True
    return False


nums = set()
for i in range(N):
    if is_good(A[i]):
        nums.add(A[i])

    for j in range(i + 1, N):
        num = A[i] + A[j]
        if is_good(num):
            nums.add(num)

        for k in range(j + 1, N):
            num = A[i] + A[j] + A[k]
            if is_good(num):
                nums.add(num)

print(len(nums))
