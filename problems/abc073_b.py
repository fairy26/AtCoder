N = int(input())
sheats = 0
for _ in range(N):
    l, r = map(int, input().split())
    sheats += r - l + 1

print(sheats)
