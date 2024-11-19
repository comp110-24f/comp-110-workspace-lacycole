from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:  # magic method
        """Represent a Node object as a string."""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)  # calls __str__
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def sum(head: Node | None) -> int:
    if head is None:
        return 0
    else:
        rest: int = sum(head.next)
        return head.value + rest


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a linked list."""
    if head.next is None:
        return head.value  # base case
    else:
        rest: int = last(head.next)
        print(f"last({head.value}) is {rest})")
        return rest  # recursive case


print(to_str(one))  # Expect 2
print(to_str(courses))  # Expect 301


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start up until end (not inclusive)"""
    # Edge case
    if start > end:
        raise ValueError("Invalid use of recursive_range")
    if start == end:
        return None
    else:
        # Recursive Case
        # Intuition: handle the first case based on a specific call
        first: int = start
        # Build the rest of the list using the builder function recursively
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)


a: Node | None = recursive_range(2, 8)
b: Node | None = recursive_range(110, 112)
print(a)
print(b)
