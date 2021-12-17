def solution(x1, x2, y1, y2):
    global highest

    highest = float('-inf')

    def loop(dx, dy):
        global highest

        px, py = 0, 0
        while True:
            px, py = px + dx, py + dy
            if py > highest:
                highest = py

            if px > x2 or py < y1:
                break

            dx, dy = max(dx - 1, 0), dy - 1

    for dx in xrange(1, x2):
        for dy in xrange(1, abs(y1)):
            loop(dx, dy)

    return highest


def parse(input):
    xs, ys = input.split()[2].strip(","), input.split()[3]
    x1, x2 = map(int, xs.split("=")[1].split(".."))
    y1, y2 = map(int, ys.split("=")[1].split(".."))
    return min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
