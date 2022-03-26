# https://qiita.com/drken/items/fd4e5e3630d0f5859067#%E7%AC%AC-4-%E5%95%8F--abc-087-b---coins-200-%E7%82%B9
A = int(input())
B = int(input())
C = int(input())
X = int(input())

answers = 0
for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            if 500 * a + 100 * b + 50 * c == X:
                answers += 1
print(answers)
