# B - Unique Nicknames
# https://atcoder.jp/contests/abc247/submissions/30873603
N = int(input())
st = [input().split() for _ in range(N)]

names = {}
for i in range(N):
    if st[i][0] not in names:
        names[st[i][0]] = 1
    else:
        names[st[i][0]] += 1

    if st[i][1] not in names:
        names[st[i][1]] = 1
    else:
        names[st[i][1]] += 1

ok = True
for i in range(N):
    if names[st[i][0]] > 1 and names[st[i][1]] > 1:
        if names[st[i][0]] == 2 and st[i][0] == st[i][1]:  # 姓と名が同じ人がいたらOK
            continue
        else:
            ok = False
            break

print("Yes" if ok else "No")
