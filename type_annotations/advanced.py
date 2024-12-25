# buffer
"""
TODO:

Annotate the function `read_buffer`, which accepts anything that is a buffer.

See https://docs.python.org/3.12/reference/datamodel.html#object.__buffer__
"""
from typing_extensions import Buffer


def read_buffer(b: Buffer): ...


# callable-protocol
"""
TODO:

Define a callable type that accepts a string parameter called `name` and returns None.
"""

from typing import Protocol


class SingleStringInput(Protocol):
    def __call__(self, *, name: str) -> None: ...


# forward
from __future__ import annotations


class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x

    # TODO: Fix the type hints of `copy` to make it type check
    def copy(self) -> MyClass:
        copied_object = MyClass(x=self.x)
        return copied_object
