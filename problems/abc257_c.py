#  解答1: WA x 14
#  逐次的に調べていき、値が変わらないときはスコアとしてみなしてはいけない
#  これを失念していた
# from bisect import bisect

# child = "0"
# adalt = "1"

# N = int(input())
# S = input()  # 0: child, 1: adalt
# W = list(map(int, input().split()))

# people = sorted([[i, w] for i, w in zip(S, W)], key=lambda x: x[1])
# sorted_S = [i for i, _ in people]

# sum_children = bisect(sorted(S), child)  # O(2log(N))

# num_children = 0
# num_mistakes = 0
# scores = [N] * (N + 1)
# scores[0] -= sum_children
# for i in range(1, N + 1):
#     if sorted_S[i - 1] == child:
#         num_children += 1
#     else:
#         num_mistakes += 1
#     scores[i] -= (sum_children - num_children) + num_mistakes

# print(max(scores))

#  解法2: AC
child = 0

N = int(input())
S = list(map(int, list(input())))  # 0: child, 1: adalt
W = list(map(int, input().split()))

people = sorted(list(zip(S, W)), key=lambda x: x[1])
f_value = sum(S)  # num of adalts
best = f_value
for idx, (i, w) in enumerate(people):
    if i == child:
        f_value += 1
    else:
        f_value -= 1

    if idx == N - 1:
        best = max(best, f_value)
    else:
        if w != people[idx + 1][1]:
            best = max(best, f_value)
print(best)
