# any
"""
TODO:

Modify `foo` so it takes an argument of arbitrary type.
"""
from typing import Any


def foo(x: Any):
    """⬆️ Change me. No need to implement the function."""


foo(1)
foo("10")


# dict
"""
TODO:

foo should accept a dict argument, both keys and values are string.
"""


def foo(x: dict[str, str]):  # type: ignore[no-redef]
    pass


foo({"foo": "bar"})
try:
    foo({"foo": 1})
except TypeError:
    assert True
else:
    assert False


# final
"""
TODO:

Make sure `my_list` cannot be re-assigned to.
"""
from typing import Final

my_list: Final = []


my_list.append(1)


# kwargs
"""
TODO:

`foo` takes keyword arguments of type integer or string.
"""


def foo1(**kwargs: int | str): ...  # type: ignore[no-redef]


foo1(a=1, b="2")


# list
"""
TODO:

foo should accept a list argument, whose elements are string.
"""


def foo(x: list[str]):  # type: ignore[no-redef]
    pass


foo(["foo", "bar"])


# optional
"""
TODO:

foo can accept an integer argument, None or no argument at all.
"""


def foo2(x: int | None = None):  # type: ignore[no-redef]
    pass


foo2(10)
foo2(None)
foo2()


# parameter
"""
TODO:

foo should accept an integer argument.
"""


def foo(x: int):  # type: ignore[no-redef]
    pass


foo(10)
try:
    foo("10")
except TypeError:
    assert True
else:
    assert False


# return
"""
TODO:

foo should return an integer argument.
"""


def foo4() -> int:  # type: ignore[no-redef]
    return 1


from typing import assert_type

assert_type(foo4(), int)


# tuple
"""
TODO:

foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
"""


def foo3(x: tuple[str, int]):  # type: ignore[no-redef]
    pass


foo3(("foo", 1))


# tipealias
"""
TODO:

Create a new type called Vector, which is a list of float.
"""
Vector = list[float]


def foo(v: Vector): ...  # type: ignore[no-redef]


foo([1.1, 2])
foo(("foo", 1))

try:
    foo(1)
    foo(["1"])
except TypeError:
    assert True
else:
    assert False


# union
"""
TODO:

foo should accept a argument that's either a string or integer.
"""
from typing import Union


def foo(x: Union[int, str]):  # type: ignore[no-redef]
    pass


foo("foo")
foo(1)

try:
    foo([])
except TypeError:
    assert True
else:
    assert False


# variable
"""
TODO:

`a` should be an integer.
"""

a: int

a = 2
