def solution(lines):

    def first_illegal(line):
        m = {")": "(", "]": "[", "}": "{", ">": "<"}

        stack = []
        for ch in line:
            if ch in m:
                if len(stack) == 0 or stack[-1] != m[ch]:
                    return ch
                else:
                    stack.pop()
            else:
                stack.append(ch)
        return None

    cost = {")": 3, "]": 57, "}": 1197, ">": 25137}

    res = 0
    for line in lines:
        ill = first_illegal(line)
        if ill is not None:
            res += cost[ill]
    return res


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
