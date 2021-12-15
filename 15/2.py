import heapq

def solution(graph):
    n = len(graph)

    graph2 = []
    for i in xrange(0, 5*n):
        graph2.append([0] * (5 * n))

        for j in xrange(0, 5*n):
            graph2[i][j] = graph[i%n][j%n] + (i/n + j/n)
            if graph2[i][j] > 9:
                graph2[i][j] = graph2[i][j] % 9

    graph = graph2

    dist_to = {}

    heap = []
    heapq.heappush(heap, (0, (0, 0)))

    while len(heap) > 0:
        dist, coord = heapq.heappop(heap)

        if coord not in dist_to:
            dist_to[coord] = dist

        i, j = coord

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for di, dj in dirs:
            ii, jj = i+di, j+dj

            if ii < 0 or ii >= len(graph) or jj < 0 or jj >= len(graph[ii]):
                continue

            dd = graph[ii][jj] + dist

            if (ii, jj) not in dist_to or dd < dist_to[(ii, jj)]:
                dist_to[(ii, jj)] = dd
                heapq.heappush(heap, (dd, (ii, jj)))

    return dist_to[(len(graph)-1, len(graph[0])-1)]


def parse(input):
    return [map(int, s) for s in input.splitlines()]


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
