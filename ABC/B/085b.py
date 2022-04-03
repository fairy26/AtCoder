N = int(input())

mochis = []
X = 0
for i in range(N):
    mochis.append(int(input()))

mochis.sort()

ex = 0
i = N - 1
while i >= 0:
    if ex != mochis[i]:
        ex = mochis[i]
    else:
        mochis.pop(i)
    i -= 1

print(len(mochis))
