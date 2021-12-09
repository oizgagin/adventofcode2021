import itertools


def solution(heightmap):

    def get_neighs(i, j):
        neighs = []
        if i-1 >= 0: neighs.append((heightmap[i-1][j], (i-1, j)))
        if i+1 < len(heightmap): neighs.append((heightmap[i+1][j], (i+1, j)))
        if j-1 >= 0: neighs.append((heightmap[i][j-1], (i, j-1)))
        if j+1 < len(heightmap[i]): neighs.append((heightmap[i][j+1], (i, j+1)))
        return neighs

    def dfs(i, j, visited):
        visited[(i, j)] = True

        for neigh in get_neighs(i, j):
            if neigh[0] == 9: continue
            if neigh[1] in visited: continue
            dfs(neigh[1][0], neigh[1][1], visited)

    basins = []
    for i in xrange(0, len(heightmap)):
        for j in xrange(0, len(heightmap[i])):
            if all(heightmap[i][j] < neigh[0] for neigh in get_neighs(i, j)):
                visited = dict()
                dfs(i, j, visited)
                basins.append(len(visited))

    return reduce(lambda acc, x: acc * x, sorted(basins)[-3:], 1)


def parse(input):
    return [map(int, line) for line in input.splitlines()]


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
