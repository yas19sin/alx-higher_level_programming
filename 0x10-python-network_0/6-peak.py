#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(lst):
    """Finds a peak in lst"""
    if not lst:
        return None
    lo, hi = 0, len(lst) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] < lst[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lst[lo]
