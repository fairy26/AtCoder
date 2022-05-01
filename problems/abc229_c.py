#  解法1
# N, W = map(int, input().split())

# AB = [list(map(int, input().split())) for _ in range(N)]

# AB = sorted(AB, key=lambda x: x[0], reverse=True)

# ans = 0
# for a, b in AB:
#     ans += a * min(b, W)
#     W -= min(b, W)
#     if W == 0:
#         break
# print(ans)

# ️ 解法2
from heapq import heappush, heappop

N, W = map(int, input().split())
cheeses = []
for _ in range(N):
    a, b = map(int, input().split())
    heappush(cheeses, (-a, b))

ans = 0
while cheeses:
    a, b = heappop(cheeses)
    ans += -a * min(b, W)
    W -= min(b, W)
    if W == 0:
        break

print(ans)
