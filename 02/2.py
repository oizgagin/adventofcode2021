def solution(commands):
    horizontal, depth, aim = 0, 0, 0

    for command in commands:
        if command[0] == "forward":
            horizontal += command[1]
            depth += aim * command[1]
        if command[0] == "up":
            aim -= command[1]
        if command[0] == 'down':
            aim += command[1]

    return depth * horizontal


def parse(input):
    return map(lambda t: (t[0], int(t[1])), map(lambda s: tuple(s.strip().split()), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
