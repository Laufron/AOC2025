from functools import reduce
from pathlib import Path

FILE = Path(__file__)
INPUT = Path("inputs") / f"{FILE.stem}.txt"


def compute(buffers: list[list[int]], ops: list[str]) -> int:
    results = []
    for op, buffer in zip(ops, buffers):

        def operation(x: int, y: int) -> int:
            match op:
                case "+":
                    return x + y
                case "*":
                    return x * y
                case _:
                    raise ValueError

        results.append(reduce(operation, buffer))

    return sum(results)


def part1():
    with INPUT.open("r") as fp:
        lines = fp.read().splitlines()
        ops = lines[-1].strip().split()
        buffers = [[] for _ in range(len(ops))]
        for line in lines[:-1]:
            for i, num in enumerate(line.split()):
                buffers[i].append(int(num))

        print(compute(buffers, ops))


def part2():
    # Input parsing is not trivial cause we want to keep column-alignment
    with INPUT.open("r") as fp:
        lines = fp.read().splitlines()

        # Parse ops while retrieving column size
        ops = []
        column_sizes = []
        count = 0
        for c in lines[-1]:
            if c != " ":
                ops.append(c)
                if count != 0:
                    column_sizes.append(count)
                    count = 0
            else:
                count += 1
        column_sizes.append(count + 1)

        buffers = [[] for _ in range(len(ops))]
        buffer_size = len(lines) - 1

        # Parsing operation members column wise (cannot use split method)
        start_char_index = 0
        for i, column_size in enumerate(column_sizes):
            for index in reversed(range(column_size)):
                num = ""
                for j in range(buffer_size):
                    num += lines[j][start_char_index + index]
                buffers[i].append(int(num.replace(" ", "")))

            start_char_index = start_char_index + column_size + 1
        print(compute(buffers, ops))


if __name__ == "__main__":
    part1()
    part2()
