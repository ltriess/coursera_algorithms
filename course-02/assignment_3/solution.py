#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Median Maintenance """

import math


def _get_parent(key: int):
    if key == 0:
        return 0
    else:
        return (key + 1) // 2 - 1


def _get_children(key: int):
    return 2 * key + 1, 2 * key + 2


class MaxHeap:
    def __init__(self):
        self._arr = []

    def insert(self, elem: int):
        self._arr.append(elem)
        self._bubble_up(len(self._arr) - 1)

    def extract_max(self) -> int:
        root = self._arr.pop(0)
        self._arr.insert(0, self._arr.pop(-1))
        self._bubble_down(0)
        return root

    def get_max(self):
        if len(self._arr) > 0:
            return self._arr[0]
        else:
            return -math.inf

    def get_size(self):
        return len(self._arr)

    def _bubble_up(self, key: int):
        parent = _get_parent(key)
        elem = self._arr[key]
        if elem > self._arr[parent]:
            self._arr[key] = self._arr[parent]
            self._arr[parent] = elem
            self._bubble_up(parent)

    def _bubble_down(self, key: int):
        children = _get_children(key)
        num_elems = len(self._arr)
        elem = self._arr[key]

        if children[0] >= num_elems:
            return
        elif children[1] >= num_elems:
            if elem > self._arr[children[0]]:
                self._arr[key] = self._arr[children[0]]
                self._arr[children[0]] = elem
                self._bubble_down(children[0])
        else:
            c0 = self._arr[children[0]]
            c1 = self._arr[children[1]]

            if c0 > c1:
                if elem < c0:
                    self._arr[key] = c0
                    self._arr[children[0]] = elem
                    self._bubble_down(children[0])
            else:
                if elem < c1:
                    self._arr[key] = c1
                    self._arr[children[1]] = elem
                    self._bubble_down(children[1])


class MinHeap:
    def __init__(self):
        self._arr = []

    def insert(self, elem: int):
        self._arr.append(elem)
        self._bubble_up(len(self._arr) - 1)

    def get_min(self):
        if len(self._arr) > 0:
            return self._arr[0]
        else:
            return math.inf

    def extract_min(self) -> int:
        root = self._arr.pop(0)
        self._arr.insert(0, self._arr.pop(-1))
        self._bubble_down(0)
        return root

    def get_size(self):
        return len(self._arr)

    def _bubble_up(self, key: int):
        parent = _get_parent(key)
        elem = self._arr[key]
        if elem < self._arr[parent]:
            self._arr[key] = self._arr[parent]
            self._arr[parent] = elem
            self._bubble_up(parent)

    def _bubble_down(self, key: int):
        children = _get_children(key)
        num_elems = len(self._arr)
        elem = self._arr[key]

        if children[0] >= num_elems:
            return
        elif children[1] >= num_elems:
            if elem < self._arr[children[0]]:
                self._arr[key] = self._arr[children[0]]
                self._arr[children[0]] = elem
                self._bubble_down(children[0])
        else:
            c0 = self._arr[children[0]]
            c1 = self._arr[children[1]]

            if c0 < c1:
                if elem > c0:
                    self._arr[key] = c0
                    self._arr[children[0]] = elem
                    self._bubble_down(children[0])
            else:
                if elem > c1:
                    self._arr[key] = c1
                    self._arr[children[1]] = elem
                    self._bubble_down(children[1])


def main(numbers: list):

    high_heap = MinHeap()  # stores higher half of elements
    low_heap = MaxHeap()  # stores lower half of elements

    median_sum = 0
    for n in numbers:
        if n <= low_heap.get_max():
            low_heap.insert(n)
        else:
            high_heap.insert(n)

        if low_heap.get_size() > high_heap.get_size() + 1:
            high_heap.insert(low_heap.extract_max())
        elif low_heap.get_size() + 1 < high_heap.get_size():
            low_heap.insert(high_heap.extract_min())
        else:
            pass

        if high_heap.get_size() > low_heap.get_size():
            median = high_heap.get_min()
        elif high_heap.get_size() < low_heap.get_size():
            median = low_heap.get_max()
        else:
            median = low_heap.get_max()

        median_sum += median

    return median_sum


if __name__ == "__main__":
    fname = "input.txt"

    with open(fname, mode="r") as fin:
        data = [int(x.strip()) for x in fin.readlines() if x.strip()]

    result = main(data)
    print("result:", result % 10000)
