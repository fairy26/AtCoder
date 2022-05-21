N = int(input())

reels = [input() for _ in range(N)]

indices = [[-1] * N for _ in range(10)]

for i in range(10):
    for j in range(N):
        idx = int(reels[j][i])
        indices[idx][j] = i

for i, nums in enumerate(indices):
    duplicated = [0] * 10
    unique = []
    for j, num in enumerate(nums):
        if num not in unique:
            unique.append(num)
        else:
            duplicated[num] += 1
        nums[j] += duplicated[num] * 10

time = [max(nums) for nums in indices]
print(min(time))
