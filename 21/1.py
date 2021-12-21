def solution(p1, p2):

    rolls = {'total': 0}

    def die():
        while True:
            for i in xrange(1, 101):
                rolls['total'] += 1
                yield i

    die = die()

    s1, s2 = 0, 0
    while True:
        p1 += sum(die.next() for _ in xrange(0, 3))
        p1 = (p1 - 1) % 10 + 1
        s1 += p1

        if s1 >= 1000:
            break

        p2 += sum(die.next() for _ in xrange(0, 3))
        p2 = (p2 - 1) % 10 + 1
        s2 += p2

        if s2 >= 1000:
            break

    return rolls['total'] * min(s1, s2)


def parse(input):
    lines = input.splitlines()
    p1, p2 = int(lines[0].split(':')[1]), int(lines[1].split(':')[1])
    return p1, p2


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
