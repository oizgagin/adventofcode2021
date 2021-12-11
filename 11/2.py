def solution(grid):

    def get_neighs(i, j):
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0: continue
                if i+di < 0 or i+di >= len(grid): continue
                if j+dj < 0 or j+dj >= len(grid[i+di]): continue
                yield (i+di, j+dj)

    def step():
        q = set()

        for i in xrange(0, len(grid)):
            for j in xrange(0, len(grid[i])):
                grid[i][j] += 1
                if grid[i][j] > 9:
                    q.add((i, j))

        flashed = set()

        while len(q) != 0:
            q2 = set()

            for i, j in q:
                flashed.add((i, j))

                grid[i][j] = 0

                for ni, nj in get_neighs(i, j):
                    if (ni, nj) in flashed:
                        continue

                    grid[ni][nj] += 1
                    if grid[ni][nj] > 9 and (ni, nj) not in q:
                        q2.add((ni, nj))

            q = q2

        return len(flashed)

    i = 0
    while True:
        i += 1
        if step() == 100:
            return i


def parse(input):
    return [map(int, line) for line in input.splitlines()]


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
