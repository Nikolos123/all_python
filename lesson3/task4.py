import os
import random
import string


def create(path, rows):
    if os.path.exists(path):
        print(f'file {path} exists.')
    else:
        chars = [random.choice(string.ascii_letters) for _ in range(rows)]
        numbers = [random.choice(string.digits) for _ in range(rows)]
        with open(path, 'w') as file:
            for row in zip(chars, numbers):
                file.write('{}\t{}\n'.format(*row))


def read(path):
    with open(path) as file:
        for row in file.readlines():
            print(row.strip())


if __name__ == '__main__':
    path = 'file.txt'
    rows = 10

    create(path, rows)
    read(path)