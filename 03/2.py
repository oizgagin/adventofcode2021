from collections import Counter


def solution(numbers):

    def calc(criteria):
        candidates = numbers[:]

        pos = 0
        while len(candidates) > 1:
            c = Counter(map(lambda number: number[pos], candidates))
            bit = criteria(c)
            candidates = filter(lambda number: number[pos] == bit, candidates)
            pos += 1

        return int(candidates[0], 2)

    oxygen = calc(lambda c: '0' if c['0'] > c['1'] else '1')
    c02 = calc(lambda c: '1' if c['0'] > c['1'] else '0')

    return oxygen * c02


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
