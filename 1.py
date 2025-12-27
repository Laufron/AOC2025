from pathlib import Path


FILE = Path(__file__)
INPUT = Path("inputs") / f"{FILE.stem}.txt"


def part1():
    position = 50
    password = 0
    with INPUT.open("r") as fp:
        for line in fp.readlines():
            if line:
                direction = -1 if line[0] == "L" else 1
                distance = int(line[1:])
                position = (position + direction * distance) % 100
                if position == 0:
                    password += 1
    print(password)


def part2():
    position = 50
    password = 0
    with INPUT.open("r") as fp:
        for line in fp.readlines():
            if line:
                direction = -1 if line[0] == "L" else 1
                distance = int(line[1:])

                start = position
                raw_end = start + direction * distance
                position = raw_end % 100

                password += abs(raw_end // 100)
                if start == 0 and direction == -1:
                    password -= 1
                if position == 0 and direction == -1:
                    password += 1

    print(password)


if __name__ == "__main__":
    part1()
    part2()
