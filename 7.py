from collections import defaultdict
from pathlib import Path
from typing import Literal


FILE = Path(__file__)
INPUT = Path("inputs") / f"{FILE.stem}.txt"


def compute_next_line(
    previous_line: str, line: str, fixed_choice: Literal["left", "right"] | None = None
) -> tuple[str, int]:
    next_line = ["@" for _ in range(len(line))]
    split_counter = 0
    if fixed_choice:
        assert previous_line.count("|") == 1
    for i, (current_char, next_char) in enumerate(zip(previous_line, line)):
        if current_char == "|":
            if next_char == "^":
                if not fixed_choice or fixed_choice == "left":
                    try:
                        next_line[i - 1] = "|"
                    except IndexError:
                        pass
                if not fixed_choice or fixed_choice == "right":
                    try:
                        next_line[i + 1] = "|"
                    except IndexError:
                        pass
                split_counter += 1
            else:
                next_line[i] = "|"

    for i, next_char in enumerate(line):
        if next_line[i] == "@":
            next_line[i] = next_char

    assert "@" not in next_line
    return "".join(next_line), split_counter


def part1():
    with INPUT.open("r") as fp:
        split_counter = 0
        previous_line = fp.readline().strip().replace("S", "|")
        for line in fp.readlines():
            previous_line, split_count = compute_next_line(previous_line, line.strip())
            split_counter += split_count
        print(split_counter)


def part2():
    # Optimisation réalisée car worlds était une liste au début (explosion de la complexité)
    # Problème intéressant
    with INPUT.open("r") as fp:
        worlds: dict[str, int] = {fp.readline().strip().replace("S", "|"): 1}
        for line in fp.readlines():
            line = line.strip()
            mem: dict[str, list[str | None]] = {}
            new_worlds = defaultdict(int)
            for world, count in worlds.items():
                cache = mem.setdefault(world, [None, None])
                if cache[0] is None:
                    cache[0] = compute_next_line(world, line, fixed_choice="left")[0]
                world_l = cache[0]

                if cache[1] is None:
                    cache[1] = compute_next_line(world, line, fixed_choice="right")[0]
                world_r = cache[1]

                new_worlds[world_l] += count
                if world_r != world_l:
                    new_worlds[world_r] += count

            worlds = new_worlds
        print(sum(worlds.values()))


if __name__ == "__main__":
    part1()
    part2()
