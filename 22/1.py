from collections import defaultdict


def solution(steps):
    grid = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))

    def valid(c):
        return -50 <= c <= 50

    for step in steps:
        if all(valid(c) for c in (step['x1'], step['x2'], step['y1'], step['y2'], step['z1'], step['z2'])):
            for x in xrange(step['x1'], step['x2']+1):
                for y in xrange(step['y1'], step['y2']+1):
                    for z in xrange(step['z1'], step['z2']+1):
                        grid[x][y][z] = step['on']

    res = 0
    for x in grid:
        for y in grid[x]:
            for z in grid[x][y]:
                if grid[x][y][z]:
                    res += 1
    return res


def parse(input):
    steps = []
    for line in input.splitlines():
        on = line.split()[0] == "on"
        coords = line.split()[1].split(",")
        x1, x2 = tuple(map(int, coords[0].strip("x=").split("..")))
        y1, y2 = tuple(map(int, coords[1].strip("y=").split("..")))
        z1, z2 = tuple(map(int, coords[2].strip("z=").split("..")))
        steps.append({
            "on": on,
            "x1": x1,
            "x2": x2,
            "y1": y1,
            "y2": y2,
            "z1": z1,
            "z2": z2,
        })
    return steps


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
