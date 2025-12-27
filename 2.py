import math
import re
from pathlib import Path
from typing import Iterable

FILE = Path(__file__)
INPUT = Path("inputs") / f"{FILE.stem}.txt"


RANGE_REGEX = re.compile(r"(\d+)-(\d+)")


def get_range(range_str: str) -> tuple[int, int]:
    m = re.match(RANGE_REGEX, range_str)
    if m:
        groups = m.groups()
        return int(groups[0]), int(groups[1])
    raise ValueError


def diviseurs(n: int) -> Iterable[int]:
    results = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(n // i)
    return sorted(results)


def part1():
    invalid_sum = 0
    with INPUT.open("r") as fp:
        data = fp.readline()
        id_ranges = data.strip().split(",")
        for id_range in id_ranges:
            id_start, id_end = get_range(id_range)
            for id in range(id_start, id_end + 1):
                id_str = str(id)
                id_len = len(id_str)
                if id_len % 2 == 0:
                    half = int(id_len / 2)
                    lstr_id = id_str[slice(None, half)]
                    rstr_id = id_str[slice(half, None)]
                    if lstr_id == rstr_id:
                        invalid_sum += id
        print(invalid_sum)


def part2():
    invalid_sum = 0
    with INPUT.open("r") as fp:
        data = fp.readline()
        id_ranges = data.strip().split(",")
        for id_range in id_ranges:
            id_start, id_end = get_range(id_range)
            for id in range(id_start, id_end + 1):
                id_str = str(id)
                id_len = len(id_str)
                for pattern_number in diviseurs(id_len):
                    if pattern_number != 1:
                        pattern_size = id_len // pattern_number
                        if id_str[:pattern_size] * pattern_number == id_str:
                            invalid_sum += id
                            break  # si l'ID est invalide on s'arrête, pas besoin de tester les autres motifs.

        print(invalid_sum)


if __name__ == "__main__":
    part1()
    part2()
