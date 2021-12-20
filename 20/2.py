from collections import defaultdict


def solution(enhancement, image):

    def pixel(image, i, j):
        res = 0
        for ii in xrange(i-1, i+2):
            for jj in xrange(j-1, j+2):
                res = (res << 1) | (1 if image[ii][jj] == '#' else 0)
        return res

    def enhance(image, minx, maxx, miny, maxy, step):
        next_ = defaultdict(lambda: defaultdict(lambda: '#' if i % 2 == 0 else '.'))
        for i in xrange(miny-1, maxy+2):
            for j in xrange(minx-1, maxx+2):
                next_[i][j] = enhancement[pixel(image, i, j)]
        return next_

    minx, maxx, miny, maxy = 0, len(image[0])-1, 0, len(image)-1
    for i in xrange(0, 50):
        image = enhance(image, minx, maxx, miny, maxy, i)
        minx, maxx, miny, maxy = minx-1, maxx+1, miny-1, maxy+1

    res = 0
    for i in xrange(miny, maxy+1):
        for j in xrange(minx, maxx+1):
            if image[i][j] == '#':
                res += 1
    return res


def parse(input):
    lines = input.splitlines()

    image = defaultdict(lambda: defaultdict(lambda: '.'))
    for i, line in enumerate(lines[2:]):
        for j, elem in enumerate(line):
            image[i][j] = elem

    return lines[0], image


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
