import itertools
from collections import defaultdict


def solution(polymer, insertions):

    def apply(polymer):
        next_ = defaultdict(int)
        for pair, count in polymer.iteritems():
            if pair in insertions:
                next_[pair[0] + insertions[pair]] += count
                next_[insertions[pair] + pair[1]] += count
        return next_

    for i in xrange(0, 10):
        polymer = apply(polymer)

    freqs = defaultdict(int)
    for pair, count in polymer.iteritems():
        freqs[pair[0]] += count
        freqs[pair[1]] += count

    max_, min_ = max(freqs.values()), min(freqs.values())

    if max_ % 2 != 0:
        max_ += 1

    if min_ % 2 != 0:
        min_ += 1

    return (max_ - min_) / 2


def parse(input):
    lines = input.splitlines()

    polymer = defaultdict(int)
    for t in zip(lines[0], lines[0][1:]):
        polymer[t[0]+t[1]] += 1

    insertions = {}
    for rule in lines[2:]:
        from_, to = tuple(rule.split(" -> "))
        insertions[from_] = to

    return polymer, insertions


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
