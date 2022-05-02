from itertools import zip_longest

O_ = input()
E_ = input()

print(*[o + e for o, e in zip_longest(O_, E_, fillvalue="")], sep="")
