import itertools
import heapq


def solution(transmission):

    def num2bits(num):
        b = bin(num)[2:]
        return map(int, '0' * (4 - len(b)) + b)

    def clamped(it, n):
        for i in xrange(0, n):
            next_ = it.next()
            yield next_

    def bits(transmission):
        for num in transmission:
            for bit in num2bits(num):
                yield bit

    def parse_pkt_ver(it):
        return int(''.join(map(str, (it.next() for _ in xrange(0, 3)))), 2)

    def parse_pkt_typ(it):
        return int(''.join(map(str, (it.next() for _ in xrange(0, 3)))), 2)

    def parse_subpkts_len(it):
        return int(''.join(map(str, (it.next() for _ in xrange(0, 15)))), 2)

    def parse_subpkts_cnt(it):
        return int(''.join(map(str, (it.next() for _ in xrange(0, 11)))), 2)

    def parse_opmode(it):
        return it.next()

    def parse_lit(it):
        res = []

        while True:
            fin = it.next()

            for _ in xrange(0, 4):
                res.append(it.next())

            if fin == 0:
                break

        return int(''.join(map(str, res)), 2)

    def peek(it):
        try:
            val = it.next()
        except StopIteration:
            return (False, None)
        else:
            return (True, itertools.chain([val], it))

    def parse_pkt(it):
        pkt_ver = parse_pkt_ver(it)
        pkt_typ = parse_pkt_typ(it)

        literal, subpkts = None, []

        if pkt_typ == 4:
            literal = parse_lit(it)
        else:
            opmode = parse_opmode(it)

            if opmode == 0:
                subpkts_it = clamped(it, parse_subpkts_len(it))
                while True:
                    fin, subpkts_it = peek(subpkts_it)
                    if not fin:
                        break
                    subpkts.append(parse_pkt(subpkts_it))
            else:
                subpkts_cnt = parse_subpkts_cnt(it)
                for i in xrange(0, subpkts_cnt):
                    subpkts.append(parse_pkt(it))

        return {
            "typ": pkt_typ,
            "ver": pkt_ver,
            "literal": literal,
            "subpkts": subpkts,
        }

    def traverse(pkt, cb):
        cb(pkt["typ"], pkt["ver"], pkt["literal"])
        for subpkt in pkt["subpkts"]:
            traverse(subpkt, cb)

    packet = parse_pkt(bits(transmission))

    versions = []
    traverse(packet, lambda typ, ver, literal: versions.append(ver))

    return sum(versions)


def parse(input):
    return map(lambda sym: int(sym, 16), input)


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
