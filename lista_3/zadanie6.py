from typing import Iterable


def generator(item):
    if isinstance(item, Iterable) and not isinstance(item, str):
            for el in item:
                yield from generator(el)
    else:
        yield item





print(list(generator(([1,'kot'],3, (4, 5,[7, 8, 9])))))
