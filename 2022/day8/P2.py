def viewing_distance():
    with open('input', 'r') as f:
        #parse input
        m = [list(map(int, row.split())) for row in f]

    def get_viewing_distance(x, y, dx, dy):
        distance = 0
        while 0 <= x + dx < len(m) and 0 <= y + dy < len(m) and m[x][y] > m[x+dx][y+dy]:
            distance += 1
            x += dx
            y += dy
        return distance

    scores = {}
    for x in range(len(m)):
        for y in range(len(m)):
            scores[(x, y)] = max(
                get_viewing_distance(x, y, 1, 0),
                get_viewing_distance(x, y, -1, 0),
                get_viewing_distance(x, y, 0, 1),
                get_viewing_distance(x, y, 0, -1)
            )

    return max(scores.values())
