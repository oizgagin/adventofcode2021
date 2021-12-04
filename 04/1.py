import itertools
from collections import defaultdict


def solution(numbers, boards):
    poss = defaultdict(list)
    for bi in xrange(0, len(boards)):
        for br in xrange(0, len(boards[bi])):
            for bc in xrange(0, len(boards[bi][br])):
                poss[boards[bi][br][bc]].append((bi, br, bc))

    # boardno -> boardrow -> marked count
    rows = defaultdict(lambda: defaultdict(int))
    # boardno -> boardcol -> marked count
    cols = defaultdict(lambda: defaultdict(int))

    def score(bi, marked):
        return sum(num for num in itertools.chain(*boards[bi]) if num not in set(marked))

    for i, number in enumerate(numbers):
        for coord in poss.get(number, []):
            bi, br, bc = coord

            rows[bi][br] += 1
            if rows[bi][br] == 5:
                return number * score(bi, numbers[:i+1])

            cols[bi][bc] += 1
            if cols[bi][bc] == 5:
                return number * score(bi, numbers[:i+1])


def parse(input):
    input = input.split("\n\n")

    numbers = map(int, input[0].split(","))

    boards = []
    for board in input[1:]:
        boards.append([map(int, row.split()) for row in board.splitlines()])

    return numbers, boards


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
