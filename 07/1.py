def solution(positions):
    positions.sort()

    med = positions[len(positions)/2]
    if len(positions) % 2 == 0:
        med = (positions[len(positions)/2-1] + positions[len(positions)/2]) / 2

    return sum(abs(num - med) for num in positions)


def parse(input):
    return map(int, input.split(","))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
