"""A deque (double-ended queue) implemented as a doubly linked list."""

from typing import Any, Optional

class DequeNode:
    next: Optional['DequeNode']
    prev: Optional['DequeNode']
    value: Any

    def __init__(self, value: Any):
        self.next = None
        self.prev = None
        self.value = value

class Deque:

    head: Optional[DequeNode]
    tail: Optional[DequeNode]

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value: Any):
        node = DequeNode(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def pop_head(self):
        value = self.head.value

        if self.head.next is not None:
            self.head.next.prev = None

        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return value

    def insert_tail(self, value: Any):
        node = DequeNode(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def pop_tail(self):
        value = self.tail.value

        if self.tail.prev is not None:
            self.tail.prev.next = None

        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None

        return value

    def reverse(self) -> 'Deque':
        """Reverse the deque, creating a new one in the process."""
        new_deque = Deque()

        current_node = self.tail
        while current_node is not None:
            new_deque.insert_tail(current_node.value)
            current_node = current_node.prev

        return new_deque

    def reverse_in_place(self):
        """Reverse the deque in place"""

        if self.head is None:
            # Cant reverse an empty deque
            return

        curr_node = self.head
        while curr_node is not None:
            old_next = curr_node.next
            curr_node.prev, curr_node.next = curr_node.next, curr_node.prev
            curr_node = old_next

        self.head, self.tail = self.tail, self.head


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
