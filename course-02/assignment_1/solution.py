#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Computing sizes of Strongly Connected Components (SCCs) """


from collections import defaultdict

import numpy as np
import tqdm


class Graph:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.graph = defaultdict(list)

    def add_edge(self, edge: tuple):
        self.graph[edge[0]].append(edge[1])

    def dfs_iterative(self, node: int, visited: list, scc: list):
        visited[node] = True
        stack = [node]
        while stack:
            node = stack[-1]
            done = True
            for i in self.graph[node]:
                if not visited[i]:
                    visited[i] = True
                    done = False
                    stack.append(i)
                    break
            if done:
                stack.pop()
                scc[-1].add(node)

    def dfs_recursive(self, node: int, visited: list, scc: list):
        visited[node] = True
        scc[-1].add(node)
        for i in self.graph[node]:
            if not visited[i]:
                self.dfs_recursive(i, visited, scc)

    def fill_order_iterative(self, node: int, visited: list, order: list):
        visited[node] = True
        stack = [node]
        while stack:
            node = stack[-1]
            done = True
            for i in self.graph[node]:
                if not visited[i]:
                    visited[i] = True
                    done = False
                    stack.append(i)
                    break
            if done:
                stack.pop()
                order.append(node)

    def fill_order_recursive(self, node: int, visited: list, order: list):
        visited[node] = True
        for i in self.graph[node]:
            if not visited[i]:
                self.fill_order_recursive(i, visited, order)
        order.append(node)

    def transpose(self):
        g = Graph(self.num_nodes)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge((j, i))
        return g

    def get_scc(self, mode: str):
        stack = []
        visited = [False] * self.num_nodes

        # First DFS Loop.
        for node in range(self.num_nodes):
            if not visited[node]:
                if mode == "recursive":
                    self.fill_order_recursive(node, visited, stack)
                elif mode == "iterative":
                    self.fill_order_iterative(node, visited, stack)
                else:
                    raise ValueError

        g_rev = self.transpose()
        visited = [False] * self.num_nodes

        # Second DFS Loop.
        scc = []
        while stack:
            node = stack.pop()
            if not visited[node]:
                scc.append(set())
                if mode == "recursive":
                    g_rev.dfs_recursive(node, visited, scc)
                elif mode == "iterative":
                    g_rev.dfs_iterative(node, visited, scc)
                else:
                    raise ValueError

        return scc


def main(edges, mode: str = "iterative"):
    print("Loading the data...")
    # This is actually stupid, because it takes a lot of extra time for nothing.
    # But my algo requires to know the number of nodes prior to building the graph.
    edges = [
        tuple(int(x) - 1 for x in edge.strip().split(" ") if edge.strip())
        for edge in edges
    ]
    edges = np.array(edges)
    nodes = np.unique(edges)
    num_nodes = len(nodes)

    print("Building the graph...")
    g = Graph(num_nodes)
    for edge in tqdm.tqdm(edges):
        g.add_edge(edge)

    print("Computing SCCs...")
    scc = g.get_scc(mode=mode)

    # Get the sizes of the 5 largest SCCs.
    scc = [len(x) for x in scc]
    scc.sort(reverse=True)
    scc = scc[:5]
    while len(scc) < 5:
        scc.append(0)
    print("result", ",".join(map(str, scc[:5])))


if __name__ == "__main__":
    fname = "input.txt"

    with open(fname, mode="r") as fin:
        data = fin.readlines()
    main(data)
