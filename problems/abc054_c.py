N, M = map(int, input().split())
AB = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AB[a].append(b)
    AB[b].append(a)

passed = [True] + [False] * (N - 1)


def walk(now, cnt):
    if all(passed):
        cnt += 1
        return cnt

    for next in AB[now]:
        if not passed[next]:
            passed[next] = True
            cnt = walk(next, cnt)
            passed[next] = False

    return cnt


print(walk(0, 0))
