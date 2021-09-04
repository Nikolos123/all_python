from itertools import zip_longest


def func(keys: list, values: list) -> dict:
    return dict(zip_longest(keys, values)) if len(keys) > len(values) else dict(zip(keys, values))


if __name__ == '__main__':
    lst1 = ['a', 'b', 'c', 'd', 'e']
    lst2 = [1, 2, 3]
    lst3 = [1, 2, 3, 4, 5, 6, 7]

    print(func(lst1, lst2))
    print(func(lst1, lst3))