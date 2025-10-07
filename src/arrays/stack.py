class Stack:
    def __init__(self, iterable=None) -> None:
        self._items: any = (
            iterable.copy() if iterable else []
        )  # copy to avoid shared reference

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return f"Stack({self._items})"

    def push(self, value) -> None:
        self._items.append(value)

    def pop(self) -> None | any:
        if self.is_empty():
            return None  # return None instead of raising IndexError
        return self._items.pop()

    def peek(self) -> None | any:
        if self.is_empty():
            return None  # return None instead of raising IndexError
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0
