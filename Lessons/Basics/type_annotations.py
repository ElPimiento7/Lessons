# https://docs.python.org/3/library/typing.html#module-typing

from typing import List, Union, Optional, Any


def calc(a: Optional[int, float], b: Any) -> Any:
    return a + b


def to_int(a_list: List[str]) -> List[int]:
    return [int(e) for e in a_list]


if __name__ == '__main__':
    to_int(["1", "2"])
    print(calc(1.2, 3.3))
