"""Module for visualizing heap data structures using NetworkX
   and Matplotlib."""

import uuid
import heapq
import random
from typing import List
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    """Class representing a node in a binary tree."""
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Recursively add edges to the graph for visualization."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root: Node) -> None:
    """Draws the binary tree using NetworkX and Matplotlib."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_binary_tree(arr: List[int]) -> Node:
    """Builds a complete binary tree from array of values."""

    if not arr:
        return None

    # Create Node objects for each value
    nodes = [Node(v) for v in arr]

    # Connect children
    for i in range(len(arr)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(arr):
            nodes[i].left = nodes[left_index]

        if right_index < len(arr):
            nodes[i].right = nodes[right_index]

    return nodes[0]


def draw_heap(arr: List[int], max_heap: bool = False) -> None:
    """Draw heap representation of the given array."""
    if max_heap:
        arr = [-x for x in arr]
    heapq.heapify(arr)
    if max_heap:
        arr = [-x for x in arr]
    root = build_binary_tree(arr)
    draw_tree(root)


if __name__ == "__main__":
    ARR_SIZE = 15
    test_arr = [random.randint(0, 100) for _ in range(ARR_SIZE)]
    print("Maximum heap representation")
    draw_heap(test_arr, max_heap=True)
    print("Minimum heap representation")
    draw_heap(test_arr, max_heap=False)
