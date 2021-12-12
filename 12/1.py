from collections import defaultdict


def solution(graph):
    global paths
    paths = 0

    def dfs(cave, smalls):
        global paths

        if cave == "end":
            paths = paths + 1
            return

        for neigh in graph[cave]:
            if neigh == "start":
                continue

            if neigh.islower() and neigh in smalls:
                continue

            if neigh.islower():
                smalls.add(neigh)
                dfs(neigh, smalls)
                smalls.remove(neigh)

            else:
                dfs(neigh, smalls)

    dfs('start', set())

    return paths


def parse(input):
    graph = defaultdict(list)
    for line in input.splitlines():
        a, b = tuple(line.split("-"))
        graph[a].append(b)
        graph[b].append(a)
    return graph


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
