"""Exercise to write functions with recursion and linked-lists."""

from __future__ import annotations

__author__ = "730735704"


class Node:
    """Making a class for Nodes."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """New node with value and next."""
        self.value = value  # sets self.value as value
        self.next = next  # sets self.next as next


def value_at(head: Node | None, index: int) -> int:
    """Returns the data of a Node stored at a given index."""
    if head is None:  # edge case
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # base case - will have reached the index of the value
        return head.value
    else:  # recursion case
        val: int = value_at(head.next, index - 1)  # calls value_at
        return val


def max(head: Node | None) -> int:
    """Returns the maximum data value in a linked list."""
    if head is None:  # edge case
        raise ValueError("Cannot call max with None")
    if head.next is None:  # for if there is only one node
        return head.value
    next_max = max(head.next)  # calls max with next head
    if head.value < next_max:  # checks if current value is less then max
        return next_max  # current value is less than max
    else:
        return head.value  # current value is greater than max


def to_str(head: Node | None) -> str:  # wrote this in class
    """Represent a Linked List as a str for linkify and scale."""
    # Used this function to print linkify and scale to test if they were working
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"  # example: 4 -> 5 -> 6 -> None


def linkify(items: list[int]) -> Node | None:
    """Returns a Linked List of Nodes with the values and orders of the input list."""
    if len(items) == 0:  # if there are no items in the list
        return None
    elif len(items) == 1:  # if there is only one item in the list
        return Node(items[0], None)
    else:  # if there are multiple items in the list
        current = items[0]  # sets current as the first value in the list
        items.pop(0)  # pops the first item from the list
        return Node(current, linkify(items))  # calls linkify with mutated list


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a linked list of Nodes where each value is scaled by the factor."""
    if head is None:  # base case
        return None
    else:  # recursive case
        new_value = head.value * factor  # multiplies the value by the factor
        next_node = scale(head.next, factor)  # calls scale on the next head
        return Node(new_value, next_node)  # returns a node with the scaled values
