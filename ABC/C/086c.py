def check(dt: int, d: int) -> bool:
    if dt < d:  # 時間が足りないので不可能
        return False
    elif (dt - d) % 2 != 0:  # 最短で行った後に調整できないので不可能
        return False
    else:
        return True


N = int(input())

# init
ok = True
t_now = 0
(x_now, y_now) = (0, 0)

for _ in range(N):
    # get input
    (t_next, x_next, y_next) = list(map(int, input().split()))

    # calcurate time, distance
    dt = t_next - t_now
    d = abs(x_next - x_now) + abs(y_next - y_now)

    # check
    ok = check(dt, d)
    if not ok:
        break

    # update
    t_now = t_next
    x_now = x_next
    y_now = y_next

# output
print("Yes" if ok else "No")
