# B - Palace
N = int(input())
T, A = map(int, input().split())
Hs = list(map(int, input().split()))

temps = [abs(A - (T - x * 0.006)) for x in Hs]
min_i = temps.index(min(temps)) + 1

print(min_i)
