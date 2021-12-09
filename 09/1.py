import itertools


def solution(heightmap):

    def get_neighs(i, j):
        neighs = []
        if i-1 >= 0: neighs.append(heightmap[i-1][j])
        if i+1 < len(heightmap): neighs.append(heightmap[i+1][j])
        if j-1 >= 0: neighs.append(heightmap[i][j-1])
        if j+1 < len(heightmap[i]): neighs.append(heightmap[i][j+1])
        return neighs

    res = 0
    for i in xrange(0, len(heightmap)):
        for j in xrange(0, len(heightmap[i])):
            if all(heightmap[i][j] < neigh for neigh in get_neighs(i, j)):
                res += heightmap[i][j] + 1
    return res


def parse(input):
    return [map(int, line) for line in input.splitlines()]


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
