def solution(measurements):
    increases = 0
    for i in xrange(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            increases += 1
    return increases


def parse(input):
    return map(int, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
