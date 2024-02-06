#!/usr/bin/python3
class MyInt(int):
    """A class representing an integer with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the inequality operator."""
        return super().__eq__(other)
