from collections import defaultdict


def solution(coords):
    horizontal = filter(lambda cs: cs[0][1] == cs[1][1], coords)
    vertical = filter(lambda cs: cs[0][0] == cs[1][0], coords)

    grid = defaultdict(lambda: defaultdict(int))

    for ps in horizontal:
        p1, p2 = ps
        if p2[0] < p1[0]:
            p1, p2 = p2, p1

        y = p1[1]
        for x in xrange(p1[0], p2[0]+1):
            grid[x][y] += 1

    for ps in vertical:
        p1, p2 = ps
        if p2[1] < p1[1]:
            p1, p2 = p2, p1

        x = p1[0]
        for y in xrange(p1[1], p2[1]+1):
            grid[x][y] += 1

    total = 0
    for x in grid:
        for y in grid[x]:
            if grid[x][y] > 1:
                total += 1
    return total


def parse(input):
    coords = []
    for line in input.splitlines():
        p1, p2 = map(str.strip, line.split("->"))
        coords.append(
            tuple(tuple(map(int, p.split(','))) for p in [p1, p2])
        )
    return coords


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
