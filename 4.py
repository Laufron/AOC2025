from pathlib import Path

FILE = Path(__file__)
INPUT = Path("inputs") / f"{FILE.stem}.txt"


def part1():
    result = 0
    with INPUT.open("r") as fp:
        data = fp.read().splitlines()
        height = len(data)
        width = len(data[0])
        for x in range(width):
            for y in range(height):
                if data[y][x] != "@":
                    continue
                roll_count = 0
                for xshift in [-1, 0, 1]:
                    for yshift in [-1, 0, 1]:
                        if xshift == 0 and yshift == 0:
                            continue

                        x_neighbour = x + xshift
                        y_neighbour = y + yshift
                        if (
                            0 <= x_neighbour < width
                            and 0 <= y_neighbour < height
                            and data[y_neighbour][x_neighbour] == "@"
                        ):
                            roll_count += 1
                if roll_count < 4:
                    result += 1

    print(result)


def replace(s: str, index: int, value: str) -> str:
    new_s = ""
    for i in range(len(s)):
        if i == index:
            new_s += value
        else:
            new_s += s[i]
    return new_s


def part2():
    total = 0
    with INPUT.open("r") as fp:
        data = fp.read().splitlines()
        height = len(data)
        width = len(data[0])
        can_remove = True
        while can_remove:
            step_total = 0
            for x in range(width):
                for y in range(height):
                    if data[y][x] != "@":
                        continue
                    roll_count = 0
                    for xshift in [-1, 0, 1]:
                        for yshift in [-1, 0, 1]:
                            if xshift == 0 and yshift == 0:
                                continue

                            x_neighbour = x + xshift
                            y_neighbour = y + yshift
                            if (
                                0 <= x_neighbour < width
                                and 0 <= y_neighbour < height
                                and data[y_neighbour][x_neighbour] in ["@", "R"]
                            ):
                                roll_count += 1

                    if roll_count < 4:
                        step_total += 1
                        data[y] = replace(data[y], x, "R")

            for y in range(height):
                data[y] = data[y].replace("R", ".")

            total += step_total
            if step_total == 0:
                can_remove = False

    print(total)


if __name__ == "__main__":
    part1()
    part2()
