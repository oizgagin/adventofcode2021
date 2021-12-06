from collections import defaultdict


def solution(timers):
    curr = [0] * 9
    for timer in timers:
        curr[timer] += 1

    def tick(curr):
        next = [0] * 9
        for i in xrange(1, 9):
            next[i-1] = curr[i]
        next[6] += curr[0]
        next[8] += curr[0]
        return next

    for i in xrange(80):
        curr = tick(curr)

    return sum(curr)


def parse(input):
    return map(int, input.split(","))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
