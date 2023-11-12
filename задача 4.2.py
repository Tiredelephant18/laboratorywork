import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    list_ = []
    with open(INPUT_FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_.append(row)
    with open(OUTPUT_FILENAME, 'w') as fa:
        json.dump(list_, fa, indent=4)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
