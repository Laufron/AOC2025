from pathlib import Path

FILE = Path(__file__)
INPUT = Path("inputs") / f"{FILE.stem}.txt"


def output_joltage(battery_number: int):
    #  I guessed part 2
    total_joltage = 0
    with INPUT.open("r") as fp:
        for bank in fp.readlines():
            bank = bank.strip()
            batteries = [int(c) for c in bank.strip()]

            n = battery_number
            chosen_indices = []
            while n > 0:
                if chosen_indices:
                    store_max_index = chosen_indices[-1] + 1
                    max_joltage = batteries[store_max_index]
                else:
                    store_max_index = 0
                    max_joltage = batteries[0]

                for i in range(store_max_index + 1, len(batteries) + 1 - n):
                    joltage = batteries[i]
                    if joltage > max_joltage:
                        store_max_index = i
                        max_joltage = joltage
                chosen_indices.append(store_max_index)
                n -= 1

            total_joltage += int("".join([bank[ind] for ind in chosen_indices]))

        print(total_joltage)


if __name__ == "__main__":
    output_joltage(2)
    output_joltage(12)
