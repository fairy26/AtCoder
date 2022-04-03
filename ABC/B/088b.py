N = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

Alice = 0
Bob = 0
for i in range(N):
    if i % 2 == 0:
        Alice += nums[i]
    else:
        Bob += nums[i]

print(Alice - Bob)
