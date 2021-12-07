import math


def solution(positions):

    def asum(lo, hi):
        return (hi + lo) * (hi - lo + 1) / 2

    res = float('inf')
    for p in xrange(1, max(positions)+1):
        r = sum(asum(0, abs(pos-p)) for pos in positions)
        if r < res:
            res = r
    return res


def parse(input):
    return map(int, input.split(","))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
