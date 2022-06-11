import math

MAX_INT = 10 ** 9


def distance(location_a, location_b):
    x_a, y_a = location_a
    x_b, y_b = location_b
    return math.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)


N, K = map(int, input().split())
A = tuple(map(int, input().split()))
torches = []
dark_persons = []
for i in range(N):
    if (i + 1) in A:
        torches.append(tuple(map(int, input().split())))
    else:
        dark_persons.append(tuple(map(int, input().split())))

dists = [MAX_INT] * len(dark_persons)
for i, location in enumerate(dark_persons):
    for torch in torches:
        dist = distance(location, torch)
        dists[i] = min(dist, dists[i])

print(max(dists))
