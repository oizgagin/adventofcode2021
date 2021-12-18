import json


def solution(nums):

    typeint = type(1)

    def split(num):
        if type(num) == typeint:
            if num >= 10:
                return [num / 2, num - num/2], True
            else:
                return num, False

        lsplit, lwas = split(num[0])
        if lwas:
            num[0] = lsplit
            return num, True

        rsplit, rwas = split(num[1])
        if rwas:
            num[1] = rsplit
            return num, True

        return num, False

    def flatten(num):
        global parents
        global curr

        parents, curr = dict(), 0

        def dfs(num, parent, left):
            global parents
            global curr

            if type(num) == typeint:
                parents[curr] = (parent, left)
                curr += 1
                return

            dfs(num[0], num, True)
            dfs(num[1], num, False)

        dfs(num, None, False)
        return parents

    def explode_find(num):
        global curr, el, er
        curr, el, er = 0, None, None

        def dfs(num, depth):
            global curr, el, er

            if (
                depth > 3 and
                type(num) == type([]) and
                type(num[0]) == typeint and
                type(num[1]) == typeint and
                el is None and
                er is None
            ):
                el, er = curr, curr+1
                return

            if type(num) == typeint:
                curr += 1
                return

            dfs(num[0], depth+1)
            dfs(num[1], depth+1)

        dfs(num, 0)
        return el, er

    def explode(num):
        l, r = explode_find(num)
        if l is None:
            return num, False

        f = flatten(num)

        lp, li = f[l]
        lval = lp[0 if li else 1]

        rp, ri = f[r]
        rval = rp[0 if ri else 1]

        if l != 0:
            llp, lli = f[l-1]
            llp[0 if lli else 1] += lval

        if r != max(f.keys()):
            rrp, rri = f[r+1]
            rrp[0 if rri else 1] += rval

        def replace(n):
            if type(n) == typeint: return

            found = False
            if type(n) == type([]) and lp in n:
                for i in xrange(0, len(n)):
                    if n[i] is lp:
                        n[i] = 0
                        found = True

            if not found:
                replace(n[0])
                replace(n[1])

        replace(num)

        return num, True

    def reduce(num):
        while True:
            num, exploded = explode(num)
            if exploded:
                continue

            num, splitted = split(num)
            if splitted:
                continue

            return num

    def magnitude(num):
        if type(num) == typeint:
            return num
        return 3 * magnitude(num[0]) + 2 * magnitude(num[1])

    curr = nums[0]
    for i in xrange(1, len(nums)):
        curr = [curr, nums[i]]
        curr = reduce(curr)

    return magnitude(curr)


def parse(input):
    return map(json.loads, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
