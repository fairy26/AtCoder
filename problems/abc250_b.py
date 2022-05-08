def add_b_times(ret, string):
    for _ in range(B):
        ret += string
    return ret


def add_a_times(ret, string):
    for _ in range(A):
        ret += string
    return ret


N, A, B = map(int, input().split())

odd = ""
even = ""
for i in range(N):
    if i % 2 != 0:
        odd = add_b_times(odd, ".")
        even = add_b_times(even, "#")
    else:
        odd = add_b_times(odd, "#")
        even = add_b_times(even, ".")

for i in range(N):
    for _ in range(A):
        if i % 2 != 0:
            print(odd)
        else:
            print(even)
