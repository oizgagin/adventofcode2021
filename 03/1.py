from collections import Counter


def solution(numbers):
    gamma, epsilon = [], []

    for bits in zip(*numbers):
        c = Counter(bits)
        if c['0'] > c['1']:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')

    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
