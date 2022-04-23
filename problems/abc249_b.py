S = input()

upper = False
lower = False
duplicate = False

for i in range(len(S)):
    s = S[i]
    if s.isupper():
        upper = True
    elif s.islower():
        lower = True
    for j in range(len(S)):
        if i == j:
            continue
        if s == S[j]:
            duplicate = True

great = upper and lower and not duplicate
print('Yes' if great else 'No')
