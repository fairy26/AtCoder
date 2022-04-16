S = input()
T = ""
words = ["dreamer", "dream", "eraser", "erase"]

# reverse
S = S[::-1]
words_rev = []
for word in words:
    words_rev.append(word[::-1])

# check
i = 0
while i < len(S):
    ok = False
    for word in words_rev:
        if S[i:].startswith(word):
            T += word
            i += len(word)
            ok = True
            break
    if not ok:
        break

print("YES" if S == T else "NO")
