# C - Takahashi's Information

grid = [list(map(int, input().split())) for _ in range(3)]

max_c = 0
for row in grid:
    for c in row:
        if c > max_c:
            max_c = c

ok = False
for num in range(max_c + 1):
    a1 = num
    b1 = grid[0][0] - a1
    b2 = grid[0][1] - a1
    b3 = grid[0][2] - a1

    a2 = grid[1][0] - b1
    if a2 == grid[1][1] - b2 and a2 == grid[1][2] - b3:
        a3 = grid[2][0] - b1
        if a3 == grid[2][1] - b2 and a3 == grid[2][2] - b3:
            ok = True
            break

print("Yes" if ok else "No")
