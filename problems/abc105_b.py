N = int(input())

A = N // 4 + 1
B = N // 7 + 1
for i in range(A):
    for j in range(B):
        if i * 4 + j * 7 == N:
            print("Yes")
            exit()

print("No")
