import itertools


def solution(notes):
    p = lambda digits: (digit for digit in digits if len(digit) in [2, 3, 4, 7])
    return len(list(itertools.chain(*map(lambda note: p(note[1]), notes))))


def parse(input):
    notes = []
    for l in input.splitlines():
        pats, digs = tuple(map(str.strip, l.split("|")[0].split())), tuple(map(str.strip, l.split("|")[1].split()))
        notes.append((pats, digs))
    return notes


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
