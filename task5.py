"""Binary Tree with DFS and BFS Traversals and Visualization."""

import uuid
import random
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    """Class representing a node in a binary tree."""
    def __init__(self, key, color="#009600"):
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
        left_x = x - 1 / 2 ** layer
        pos[node.left.id] = (left_x, y - 1)
        add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)
    if node.right:
        graph.add_edge(node.id, node.right.id)
        right_x = x + 1 / 2 ** layer
        pos[node.right.id] = (right_x, y - 1)
        add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    """Draws the binary tree using NetworkX and Matplotlib."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False,
        node_size=2500, node_color=colors
    )
    plt.show()


def insert(root: Node, key) -> Node:
    """Insert key into the binary search tree rooted at root."""
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def rgb565_to_hex(rgb565: int) -> str:
    """
    Convert RGB565 color (decimal integer) to HTML/CSS #RRGGBB format.
    Args:
        rgb565: RGB565 color as decimal integer (0-65535)
    Returns:
        Color string in #RRGGBB format
    """
    if not 0 <= rgb565 <= 0xFFFF:
        raise ValueError("rgb565 must be in range 0-65535")

    # Extract RGB565 components
    r5 = (rgb565 >> 11) & 0x1F
    g6 = (rgb565 >> 5) & 0x3F
    b5 = rgb565 & 0x1F

    # Expand to 8-bit per channel (best quality)
    r8 = (r5 << 3) | (r5 >> 2)
    g8 = (g6 << 2) | (g6 >> 4)
    b8 = (b5 << 3) | (b5 >> 2)

    # Format as HTML/CSS hex color
    return f"#{r8:02X}{g8:02X}{b8:02X}"


def dfs_traversal(root, elements_num):
    """
    Depth-First Search traversal using a stack (iterative).
    Changes node colors (RGB565) during traversal. Use shades of green
    from dark to light to show the order of visiting nodes.
    Args:
        root: Root node of the binary tree
        elements_num: Total number of elements in the tree
    Returns:
        List of visited node values in DFS order
    """
    if root is None:
        return []

    visited = []
    stack = [root]
    # Initial colour in RGB565 format (dark green)
    colour = 512
    # Colour step size depends on number of elements and initial colour
    colour_step = int(48 / elements_num) if elements_num < 48 else 1

    while stack:
        # Pop from stack (LIFO - Last In First Out)
        node = stack.pop()

        if node is None:
            continue

        # Add to visited list
        visited.append(node.val)
        node.color = rgb565_to_hex(colour)
        # If tree is large, reset colour to avoid green colour overflow
        # in RGB565
        if colour == 2016:
            colour = 512
        # Make colour lighter for the next nodes
        colour += ((0 << 11) | (colour_step << 5) | 0)

        # Mark as visited (change color)
        # node.color = visited_color

        # Push right child first, then left (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


def bfs_traversal(root, elements_num):
    """
    Breadth-First Search traversal using a queue (iterative).
    Changes node colors (RGB565) during traversal. Use shades of green
    from dark to light to show the order of visiting nodes.
    Args:
        root: Root node of the binary tree
        elements_num: Total number of elements in the tree
    Returns:
        List of visited node values in BFS order
    """
    if root is None:
        return []

    visited = []
    queue = deque([root])
    # Initial colour in RGB565 (dark green)
    colour = 512
    # Colour step size depends on number of elements and initial colour
    colour_step = int(48 / elements_num) if elements_num < 48 else 1

    while queue:
        # Dequeue from front (FIFO - First In First Out)
        node = queue.popleft()
        if node is None:
            continue
        node.color = rgb565_to_hex(colour)
        # If tree is large, reset colour to avoid green colour overflow
        # in RGB565
        if colour == 2016:
            colour = 512
        # Make colour lighter for the next nodes
        colour += ((0 << 11) | (colour_step << 5) | 0)

        # Add to visited list
        visited.append(node.val)

        # Enqueue children (left first, then right)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited


def main():
    """Main function to demonstrate DFS and BFS traversals
       on a binary search tree."""
    arr_size = 10
    arr = [random.randint(0, 100) for _ in range(arr_size)]
    print("Generate Binary Search Tree with the following values:", arr)
    root = Node(arr[0])
    for value in arr[1:]:
        insert(root, value)

    # DFS traversal
    print("\nPerforming DFS traversal...")
    dfs_result = dfs_traversal(root, arr_size)
    print(f"DFS order: {dfs_result}")
    draw_tree(root)

    # BFS traversal
    print("\nPerforming BFS traversal...")
    bfs_result = bfs_traversal(root, arr_size)
    print(f"BFS order: {bfs_result}")
    draw_tree(root)


if __name__ == "__main__":
    main()
