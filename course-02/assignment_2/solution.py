#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Dijkstra's Shortest-Path Algorithm """


import numpy as np

NUM_VERT = 200
MAX_DIST = 1000000
REPORT_VERT = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]


def dijkstra(graph: np.ndarray, src: int = 0):
    distances = [MAX_DIST] * NUM_VERT
    distances[src] = 0
    processed = [False] * NUM_VERT

    for _ in range(NUM_VERT):
        # Find the minimum value index.
        min_val = MAX_DIST
        min_idx = None
        for v in range(NUM_VERT):
            if processed[v] is False and distances[v] < min_val:
                min_val = distances[v]
                min_idx = v

        if min_idx is None:
            break

        # Add minimum distance vertex to processed.
        processed[min_idx] = True

        # Update the distances of adjacent vertices of the picked vertex.
        for v in range(NUM_VERT):
            if (
                graph[min_idx, v] != -1
                and processed[v] is False
                and distances[v] > distances[min_idx] + graph[min_idx, v]
            ):
                distances[v] = distances[min_idx] + graph[min_idx, v]

    return distances


def main(graph: np.ndarray):
    distances = dijkstra(graph)
    print("result:")
    print(",".join(str(distances[node - 1]) for node in REPORT_VERT))


if __name__ == "__main__":
    fname = "input.txt"

    matrix = -1 * np.ones(shape=(NUM_VERT, NUM_VERT), dtype=np.int)
    with open(fname, mode="r") as fin:
        for _ in range(200):
            line = fin.readline().strip().split("\t")
            v_s = int(line.pop(0))
            for e in line:
                v_t, length = map(int, e.split(","))
                matrix[v_s - 1, v_t - 1] = length

    main(matrix)
