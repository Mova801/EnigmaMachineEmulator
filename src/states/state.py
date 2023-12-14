from abc import ABC, abstractmethod
from typing import Self


class State[T](ABC):
    """
    """
    _stack: list[T]

    def __getitem__(self, index: int) -> Self:
        return self._stack[index % len(self._stack)]

    @abstractmethod
    def execute(self) -> None:
        """
        Exe
        :return: None
        """

    def push(self, element: T) -> None:
        """
        inserts a new element at the top of the stack.
        :param element: element to add to the stack
        :return: None
        """
        element._stack = self._stack
        self._stack.append(element)

    def pop(self) -> T:
        """
        removes the element at the top of the stack.
        :return: element removed from the stack
        """
        return self._stack.pop()
