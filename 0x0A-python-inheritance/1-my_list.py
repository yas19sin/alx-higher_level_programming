#!/usr/bin/python3
class MyList(list):
    """Inherits from list and provides additional methods."""

    def print_sorted(self):
        """Prints the list in sorted order."""
        print(sorted(self))
