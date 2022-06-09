import heapq


N, K, X = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))

heapq.heapify(A)
while len(A) > 0 and K > 0:
    item = -heapq.heappop(A)
    if item > X:
        if item // X <= K:
            K -= item // X
            item = item % X
        else:
            item -= K * X
            K = 0

        if item > 0:
            heapq.heappush(A, -item)
    else:
        K -= 1

print(-sum(A))
