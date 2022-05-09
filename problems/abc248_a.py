S = input()

nums = [int(char) for char in S]

for i in range(10):
    if i not in nums:
        print(i)
        exit()
