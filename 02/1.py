def solution(commands):
    horizontal, depth = 0, 0

    for command in commands:
        if command[0] == "forward":
            horizontal += command[1]
        if command[0] == "up":
            depth -= command[1]
        if command[0] == 'down':
            depth += command[1]

    return depth * horizontal


def parse(input):
    return map(lambda t: (t[0], int(t[1])), map(lambda s: tuple(s.strip().split()), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
