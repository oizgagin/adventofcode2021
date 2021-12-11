def solution(lines):

    def first_illegal(line):
        m = {")": "(", "]": "[", "}": "{", ">": "<"}

        stack = []
        for ch in line:
            if ch in m:
                if len(stack) == 0 or stack[-1] != m[ch]:
                    return ch, []
                else:
                    stack.pop()
            else:
                stack.append(ch)

        return None, stack

    def score(stack):
        m = {"(": ")", "[": "]", "{": "}", "<": ">"}
        cost = {")": 1, "]": 2, "}": 3, ">": 4}

        res = 0
        for i in xrange(len(stack)-1, -1, -1):
            res = res * 5 + cost[m[stack[i]]]
        return res

    scores = []
    for line in lines:
        ill = first_illegal(line)

        if ill[0] is None:
            scores.append(score(ill[1]))

    scores.sort()
    return scores[len(scores)/2]


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
