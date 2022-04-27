S = input()
T = input()

ok = False
if S == T:
    ok = True
else:
    for i in range(len(S) - 1):
        S_ = S[:i] + S[i + 1] + S[i] + S[i + 2 :]
        if T == S_:
            ok = True
            break

print("Yes" if ok else "No")
