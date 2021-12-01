def solution(measurements):
    increases = 0

    curr = tuple(measurements[:3])
    for t in zip(measurements, measurements[1:], measurements[2:]):
        if sum(t) > sum(curr):
            increases += 1
        curr = t

    return increases


def parse(input):
    return map(int, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
