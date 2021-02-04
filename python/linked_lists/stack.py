"""A stack implemented as a singly linked list."""

from typing import Any, Optional

class EmptyStack(Exception):
    pass


class StackNode:
    next: Optional['StackNode']
    value: Any

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    head: Optional[StackNode]

    def __init__(self):
        self.head = None

    def push(self, value: Any):
        node = StackNode(value)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head is None:
            raise EmptyStack()

        top_value = self.head.value
        self.head = self.head.next

        return top_value

    def peek(self):
        return self.head.value

    def index(self, idx: int) -> Any:
        """Return the value of the node at the index"""

        if self.head is None:
            raise IndexError("List is empty")

        current_node = self.head
        curr_ndx = 0
        while current_node.next is not None and curr_ndx < idx:
            current_node = current_node.next
            curr_ndx += 1

        if curr_ndx == idx:
            return current_node.value
        else:
            raise IndexError("Index out of bounds")

    def find(self, value: Any) -> int:
        """Return the index of the node containing the value"""

        if self.head is None:
            return None

        current_node = self.head
        curr_ndx = 0
        while current_node.next is not None and current_node.value != value:
            current_node = current_node.next
            curr_ndx += 1

        if current_node.value == value:
            return curr_ndx
        else:
            return None

    def __str__(self):

        if self.head is None:
            return "[]"

        current_node = self.head
        str_parts = [f"[ {str(current_node.value)}"]
        while current_node.next is not None:
            current_node = current_node.next
            str_parts.append(f", {str(current_node.value)}")
        str_parts.append(" ]")

        return "".join(str_parts)
