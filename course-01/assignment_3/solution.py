#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Quick Sort. """

version = "median"
comparisons = 0


def choose_pivot(array: list, low: int, high: int):
    if version == "first":
        # Always first element.
        pivot = array[low]
    elif version == "last":
        # Always last element.
        pivot = array[high - 1]
        array[high - 1] = array[low]
        array[low] = pivot
    elif version == "median":
        # Median of three.
        idx_a = low
        idx_b = low + (high - 1 - low) // 2
        idx_c = high - 1
        a = array[idx_a]
        b = array[idx_b]
        c = array[idx_c]

        if a <= b <= c or a >= b >= c:
            pivot = b
            array[idx_b] = array[low]
            array[low] = pivot
        elif a <= c <= b or a >= c >= b:
            pivot = c
            array[idx_c] = array[low]
            array[low] = pivot
        else:
            pivot = a
    else:
        raise ValueError

    return pivot, array


def quick_sort(array: list, low: int = None, high: int = None):
    global comparisons

    if low is None:
        low = 0
    if high is None:
        high = len(array)

    # Base case. No sorting necessary.
    if high - low <= 1:
        return array

    # Increment by the number of comparisons in this call (== iterations of loop).
    comparisons += high - low - 1

    # Choose pivot at first position, no swap necessary here.
    pivot, array = choose_pivot(array, low, high)

    # Partitioning.
    i = low + 1
    for j in range(low + 1, high):
        elem = array[j]
        if elem < pivot:
            # Swap A[j] and A[i]
            array[j] = array[i]
            array[i] = elem
            i += 1

    # Place pivot element in correct location.
    tmp = array[i - 1]
    array[i - 1] = array[low]
    array[low] = tmp

    # Sort first part.
    array = quick_sort(array, low=low, high=i - 1)
    # Sort second part.
    array = quick_sort(array, low=i, high=high)

    return array


if __name__ == "__main__":
    fname = "input.txt"
    with open(fname, mode="r") as fin:
        data = fin.readlines()
    data = [int(x.strip()) for x in data if x.strip()]

    sorted_array = quick_sort(data)
    assert sorted_array == sorted(data), "The sorting is not correct!"
    print("result:", comparisons)
