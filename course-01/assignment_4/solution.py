#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Randomized Contraction for Min Cut """


import copy
import math
import random


def pick_edge(graph: dict) -> tuple:
    # Helper function to choose the next edge uniformly from all remaining edges.
    edges = [x for s in [[(k, x) for x in v] for k, v in graph.items()] for x in s]
    return random.choice(edges)


def karger(graph: dict) -> int:

    while len(graph) > 2:
        # Pick remaining edge (u,v) uniformly at random.
        u, v = pick_edge(graph)

        # Contract u and v into a single vertex.
        graph[u] += graph[v]
        del graph[v]
        graph = {key: [u if x == v else x for x in vals] for key, vals in graph.items()}

        # Remove self-loops.
        graph[u] = [x for x in graph[u] if x != u]

    return len(list(graph.values())[0])


if __name__ == "__main__":
    fname = "input.txt"
    with open(fname, mode="r") as fin:
        data = fin.readlines()
    data = {x[0]: x[1:] for x in (x.strip().split() for x in data if x.strip())}

    # Run multiple tries of the algorithm and store the minimum cut value.
    # I chose to let run the algorithm n times with n being the number of vertices.
    min_cut = math.inf
    for i in range(len(data)):
        count = karger(copy.deepcopy(data))
        min_cut = min(min_cut, count)
        print(
            "{0:3d} / {1:3d}: current {2:3d}, min {3:3d}".format(
                i, len(data), count, min_cut
            )
        )

    print()
    print("result:", min_cut)
