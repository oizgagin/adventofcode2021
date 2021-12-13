import itertools
from collections import defaultdict


def solution(paper, folds):

    def foldy(paper, y):
        i, j = y-1, y+1
        while i >= 0 and j < len(paper):
            paper[i] = map(lambda t: t[0] or t[1], zip(paper[i], paper[j]))
            i, j = i-1, j+1
        return paper[:lines]

    def foldx(paper, x):
        i, j = x-1, x+1
        while i >= 0 and j < len(paper[0]):
            for y in xrange(0, len(paper)):
                paper[y][i] = paper[y][i] or paper[y][j]
            i, j = i-1, j+1

        for y in xrange(0, len(paper)):
            paper[y] = paper[y][:x]

        return paper

    def fold(paper, dir, lines):
        if dir == 'y':
            return foldy(paper, lines)
        return foldx(paper, lines)

    for dir, lines in folds[:1]:
        paper = fold(paper, dir, lines)

    return sum(itertools.chain(*paper))


def parse(input):
    dots, folds = set(), []

    miny, minx = float('inf'), float('inf')
    maxy, maxx = float('-inf'), float('-inf')

    for line in input.splitlines():
        if "fold" in line:
            dir, lines = tuple(line[len("fold along "):].split("="))
            folds.append((dir, int(lines)))
        elif line != "":
            x, y = tuple(map(int, line.split(",")))
            dots.add((x, y))
            miny, maxy, minx, maxx = min(miny, y), max(maxy, y), min(minx, x), max(maxx, x)

    paper = []
    for y in xrange(miny, maxy+1):
        row = []
        for x in xrange(minx, maxx+1):
            row.append(int((x, y) in dots))
        paper.append(row)

    return paper, folds


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
