# A - Infinite Coins
N = int(input())
A = int(input())
ok = (N % 500) <= A
print("Yes" if ok else "No")
