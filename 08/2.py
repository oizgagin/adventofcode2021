import itertools


#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

def solution(notes):

    def take(it, p):
        f = filter(p, it)
        assert len(f) == 1, f
        return f[0]

    def setsub(s1, s2):
        return s1 - s2

    def setmul(s1, s2):
        return s1.intersection(s2)

    def first(s):
        assert len(s) == 1
        return list(s)[0]

    def decode(patterns):
        pat1 = take(patterns, lambda pattern: len(pattern) == 2)
        pat4 = take(patterns, lambda pattern: len(pattern) == 4)
        pat7 = take(patterns, lambda pattern: len(pattern) == 3)
        pat8 = take(patterns, lambda pattern: len(pattern) == 7)

        a = first(setsub(pat7, pat1))

        bd = setsub(pat4, pat1)

        pat0 = take(patterns, lambda pattern: len(pattern) == 6 and len(setmul(pattern, bd)) == 1)

        b = first(setmul(pat0, bd))
        d = first(setsub(bd, set([b])))

        pat5 = take(patterns, lambda pattern: len(pattern) == 5 and len(setmul(pattern, [a, b, d])) == 3)

        f = first(setmul(pat5, pat1))
        g = first(setsub(pat5, set([a, b, d, f])))
        c = first(setsub(pat4, set([b, d, f])))
        e = first(setsub(pat8, set([a, b, c, d, f, g])))

        return {
            a: 'a',
            b: 'b',
            c: 'c',
            d: 'd',
            e: 'e',
            f: 'f',
            g: 'g',
        }

    def transform(digit, m):
        return ''.join(sorted(m[ch] for ch in digit))

    d = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }

    res = 0
    for note in notes:
        m = decode(note[0])
        res += int(''.join(d[transform(digit, m)] for digit in note[1]))
    return res


def parse(input):
    notes = []
    for l in input.splitlines():
        pats = tuple(map(lambda s: set(s.strip()), l.split("|")[0].split()))
        digs = tuple(map(str.strip, l.split("|")[1].split()))
        notes.append((pats, digs))
    return notes


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
