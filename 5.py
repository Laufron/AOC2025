from typing import Iterable

from pathlib import Path

FILE = Path(__file__)
INPUT = Path("inputs") / f"{FILE.stem}.txt"


def process_range(line: str) -> Iterable[int]:
    start, end = line.split("-")
    return range(int(start), int(end) + 1)


def part1():
    fresh_ranges: list[Iterable[int]] = []
    with INPUT.open("r") as fp:
        line = fp.readline()
        while line != "\n":
            fresh_ranges.append(process_range(line.strip()))
            line = fp.readline()

        fresh = 0
        for item in fp.readlines():
            item = int(item.strip())
            for fresh_range in fresh_ranges:
                if item in fresh_range:
                    fresh += 1
                    break
    print(fresh)


def part2():
    fresh_ranges = []
    with INPUT.open("r") as fp:
        line = fp.readline()
        while line != "\n":
            fresh_ranges.append(process_range(line.strip()))
            line = fp.readline()

        # calcul de la taille de l'union des ranges
        fresh_ranges = sorted(fresh_ranges, key=lambda r: r[0])
        union_size = len(fresh_ranges[0])
        union_end = fresh_ranges[0][-1]
        for fresh_range in fresh_ranges[1:]:
            start = fresh_range[0]
            end = fresh_range[-1]
            size = len(fresh_range)
            if start > union_end:
                union_size += size
                union_end = end
            else:
                if end <= union_end:
                    continue
                else:
                    union_size = union_size + size - (union_end - start + 1)
                    union_end = end
        print(union_size)


if __name__ == "__main__":
    part1()
    part2()
