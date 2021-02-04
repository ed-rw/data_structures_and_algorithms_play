"""Implement a set that can store unsigned 16 bit integers (ushort).

Remember seeing this in a presentation somewhere. Going to try to implement
this just using the concept.

Idea is that using a series of bits (in this case a very large integer), you
flip a bit to one when the value at that index is in the set.

In this case the integer 2**65536 will be the data structure behind our set.
With the sign bit, this integer contains 65536 bits. Enough to hold the
membership details for all possible values an unsigned 16 bit integer can take.
"""

class Unsigned16BitIntSet:

    def __init__(self):
        self.set_values = 2**65536  # Initialize the empty set

    def add(self, value: int):
        if value < 0 or value > 65536:
            raise ValueError("Set values must be between 0 and 65,536")

        # Convert value to int with one flipped on at the position in bit
        # string where the index == value
        value_bitmask = 2**value

        self.set_values |= value_bitmask

    def remove(self, value: int):
        if value < 0 or value > 65536:
            raise ValueError("Set values must be between 0 and 65,536")

        value_bitmask = 2**value

        if self.contains(value):
            # If the set does not contain the value we're trying to remove
            # and we xor with the bitmask, it will add the value to the set
            self.set_values ^= value_bitmask

    def contains(self, value: int) -> bool:
        if value < 0 or value > 65536:
            raise ValueError("Set values must be between 0 and 65,536")

        value_bitmask = 2**value

        return (self.set_values & value_bitmask) != 0
