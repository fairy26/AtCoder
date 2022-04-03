inputs = list(map(int, input().split()))
N = inputs[0]
A = inputs[1]
B = inputs[2]

all_sum = 0
for i in range(N + 1):
    num = i
    num_length = len(str(num))
    num_sum = 0
    for _ in range(num_length):
        num_sum += num % 10
        num = num // 10
    if num_sum >= A and num_sum <= B:
        all_sum += i
print(all_sum)
