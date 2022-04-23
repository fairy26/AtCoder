# C - Pyramid
N = int(input())
x_y_h = [list(map(int, input().split())) for _ in range(N)]

for c_x in range(100 + 1):
    for c_y in range(100 + 1):
        # at 1st, calcurate H
        H = 1
        for i in range(N):
            x = x_y_h[i][0]
            y = x_y_h[i][1]
            h = x_y_h[i][2]
            if h > 0:
                H = abs(x - c_x) + abs(y - c_y) + h
                break
        # at 2nd, check H is ok for all x, y
        ok = True
        for i in range(N):
            x = x_y_h[i][0]
            y = x_y_h[i][1]
            h = x_y_h[i][2]
            if h != max(H - abs(x - c_x) - abs(y - c_y), 0):
                ok = False
                break
        # at 3rd, if ok, print
        if ok:
            print(c_x, c_y, H)
            exit()
