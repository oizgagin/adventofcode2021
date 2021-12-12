from collections import defaultdict


def solution(graph):
    global paths
    paths = 0

    def dfs(cave, smalls, path):
        global paths

        if cave == "end":
            paths += 1
            return

        for neigh in graph[cave]:
            if neigh == "start":
                continue

            if neigh.islower() and (smalls[neigh] == 2 or (smalls[neigh] == 1 and any(v == 2 for v in smalls.values()))):
                continue

            if neigh.islower():
                smalls[neigh] += 1
                path.append(neigh)
                dfs(neigh, smalls, path)
                path.pop()
                smalls[neigh] -= 1

            else:
                path.append(neigh)
                dfs(neigh, smalls, path)
                path.pop()

    dfs('start', defaultdict(int), list())

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
