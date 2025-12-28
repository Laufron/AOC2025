import heapq
import math
from dataclasses import dataclass
from pathlib import Path

FILE = Path(__file__)
INPUT = Path("inputs") / f"{FILE.stem}.txt"


@dataclass
class JunctionBox:
    x: int
    y: int
    z: int


def squared_distance(box1: JunctionBox, box2: JunctionBox) -> float:
    return (box1.x - box2.x) ** 2 + (box1.y - box2.y) ** 2 + (box1.z - box2.z) ** 2


def find(i, parent: list) -> int:
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]


def union(i, j, parent: list, size: list):
    ri, rj = find(i, parent), find(j, parent)
    if ri == rj:
        return
    if size[ri] < size[rj]:
        ri, rj = rj, ri
    parent[rj] = ri
    size[ri] += size[rj]


def part1():
    # Had to learn about UnionFind data structure : https://fr.wikipedia.org/wiki/Union-find for part 1
    boxes = []

    with INPUT.open("r") as fp:
        lines = fp.read().splitlines()
        for i, line in enumerate(lines):
            x, y, z = line.split(",")
            boxes.append(JunctionBox(int(x), int(y), int(z)))

    n = len(boxes)
    size = [1] * n
    parent = list(range(n))

    distances: list[tuple[float, int, int]] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distances.append((squared_distance(boxes[i], boxes[j]), i, j))

    for _, i, j in heapq.nsmallest(1000, distances, key=lambda dist: dist[0]):
        union(i, j, parent, size)

    root_sizes = {find(i, parent): size[find(i, parent)] for i in range(n)}
    print(math.prod(heapq.nlargest(3, root_sizes.values())))


def check_one_circuit(parent: list) -> bool:
    root = find(0, parent)
    for i in range(1, len(parent)):
        if find(i, parent) != root:
            return False
    return True


def part2():
    boxes = []

    with INPUT.open("r") as fp:
        lines = fp.read().splitlines()
        for i, line in enumerate(lines):
            x, y, z = line.split(",")
            boxes.append(JunctionBox(int(x), int(y), int(z)))

    n = len(boxes)
    size = [1] * n
    parent = list(range(n))

    distances: list[tuple[float, int, int]] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distances.append((squared_distance(boxes[i], boxes[j]), i, j))

    for _, i, j in sorted(distances, key=lambda dist: dist[0]):
        union(i, j, parent, size)
        if check_one_circuit(parent):
            print(boxes[i].x * boxes[j].x)
            break


if __name__ == "__main__":
    part1()
    part2()
