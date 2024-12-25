# await
"""
TODO:

`run_async` takes an awaitable integer.
"""
from typing import Awaitable


def run_async(x: Awaitable[int]):
    pass


# callable
"""
TODO:

Define a callable type that accepts a string argument and returns None.
*The parameter name can be arbitrary.*
"""
from typing import Callable

SingleStringInput = Callable[[str], None]


# class var
"""
TODO:

Class `Foo` has a class variable `bar`, which is an integer.
"""
from typing import ClassVar


class Foo:
    """Hint: No need to write __init__"""

    bar: ClassVar[int]


# empty-tuple
"""
TODO:

foo should accept a empty tuple argument.
"""


def foo(x: tuple[()]):
    pass


# generic
"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
"""
from typing import TypeVar

T = TypeVar("T", int, str, list[str])


def add(a: T, b: T) -> T:
    return a + b


# generic2
"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
"""
from typing import TypeVar

R = TypeVar("R", int, str)


def add(a: R, b: R) -> R:  # type: ignore[no-redef]
    return a + b


# generic3
"""
TODO:

The function `add` accepts one argument and returns a value, they all have the same type.
The type can only be int or subclasses of int.
"""
from typing import TypeVar

S = TypeVar("S", bound=int)


def add(a: S) -> S:  # type: ignore[no-redef]
    return a


# instance var
"""
TODO:

Class `Foo1` has an instance variable `bar`, which is an integer.
"""


class Foo1:
    """Hint: you don't need to write __init__"""

    bar: int


# literals
"""
TODO:

foo only accepts literal 'left' and 'right' as its argument.
"""
from typing import Literal

Directions = Literal["left", "right"]


def foo(direction: Directions):  # type: ignore[no-redef]
    return


# literal string
"""
TODO:

You're writing a web backend.
Annotate a function `execute_query` which runs SQL, but also can prevent SQL injection attacks.

NOTE: You don't need to implement `execute_query`
"""

from typing import Iterable, LiteralString


def execute_query(sql: LiteralString, parameters: Iterable[str] = ...):
    pass


# self
"""
TODO:

`return_self` should return an instance of the same type as the current enclosed class.
"""

import typing

Self = typing.TypeVar("Self", bound="Foo")


class Foo2:
    def return_self(self) -> typing.Self:
        return self


# typed-dict
"""
TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string
"""
from typing import TypedDict

Student = TypedDict("Student", {"name": str, "age": int, "school": str})

# typed-dict2
"""
TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string

Note: school can be optional
"""
from typing import TypedDict, NotRequired

Student = TypedDict("Student", {"name": str, "age": int, "school": NotRequired[str]})  # type: ignore[no-redef]


# typed-dict3
"""
TODO:

Define a class `Person` that represents a dictionary with five string keys:
    name, age, gender, address, email

The value of each key must be the specified type:
    name - str, age - int, gender - str, address - str, email - str

Note: Only `name` is required
"""
from typing import TypedDict, Required

Person = TypedDict(
    "Person",
    {"name": Required[str], "age": int, "gender": str, "address": str, "email": str},
    total=False,
)


# unpack
"""
TODO:

`foo` expects two keyword arguments - `name` of type `str`, and `age` of type `int`.
"""

from typing import TypedDict, Unpack


class Person(TypedDict):  # type: ignore[no-redef]
    name: str
    age: int


def foo(**kwargs: Unpack[Person]):  # type: ignore[no-redef]
    pass
