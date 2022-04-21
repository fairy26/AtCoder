# A - Duplex Printing
N = int(input())

pages = N // 2
if N % 2 == 1:
    pages += 1

# pages = (N+1) // 2
#  or
# pages = N//2 + N%2

print(pages)
