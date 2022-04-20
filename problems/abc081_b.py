# ABC081B - Shift only
N = int(input())
As = list(map(int, input().split()))

count = 0
finish = False
while True:
    for i in range(N):
        if As[i] % 2 == 0:
            As[i] = As[i] // 2
        else:
            finish = True
    if finish:
        break
    else:
        count += 1

print(count)
