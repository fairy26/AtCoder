from itertools import combinations


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

can_connect_directly = True
for num1, num2 in combinations([a, b, c, d, e], 2):
    if abs(num1 - num2) > k:
        can_connect_directly = False

print("Yay!" if can_connect_directly else ":(")
