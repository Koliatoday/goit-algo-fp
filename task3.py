"""
Dijkstra's algorithm with heap.
This implementation uses a min-heap to store the vertices and their distances.
"""
import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra_heap(graph, start):
    """
    Dijkstra's algorithm with heap
    Args:
        graph: adjacency list {node: [(neighbor, weight), ...]}
        start: starting vertex
    Returns:
        distances: dictionary of distances to all vertices
    Raises:
        KeyError:   if start node is not in the graph
        ValueError: if graph is empty or contains negative weights
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    if start not in graph:
        raise KeyError(f"Start node '{start}' not found in graph")

    # 1. Distances table
    distances = {v: float('inf') for v in graph}
    distances[start] = 0

    # 2. Min-heap (distance, vertex)
    heap = [(0, start)]

    while heap:
        current_dist, vertex = heapq.heappop(heap)

        # Ignore outdated entries
        if current_dist > distances[vertex]:
            continue

        # Traverse neighbors
        for neighbor, weight in graph[vertex]:
            if neighbor not in distances:
                # Skip if neighbor is not in the graph
                continue
            if weight < 0:
                # Dijkstra doesn't work with negative weights
                raise ValueError(
                    f"Negative weight detected: {weight} "
                    f"on edge ({vertex}, {neighbor})"
                )
            new_dist = current_dist + weight

            # Relaxation
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist

                # Push new pair into heap
                heapq.heappush(heap, (new_dist, neighbor))

    return distances


def usage_example(node: str) -> None:
    """
    Usage example for dijkstra_heap function.
    Args:
        node: starting node
    Returns:
        None
    """
    if node not in ["A", "B", "C", "D", "E"]:
        print("Invalid starting node. Must be one of: A, B, C, D, E")
        return

    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 3), ('D', 1), ('E', 3)],
        'C': [('A', 2), ('B', 3), ('D', 4), ('E', 5)],
        'D': [('B', 1), ('C', 4), ('E', 1)],
        'E': [('B', 3), ('C', 5), ('D', 1)]
    }
    distances = dijkstra_heap(graph, node)
    print(f"Shortest path from {node} to all other nodes:\n{distances}")

    # The same graph as above drawn with networkx library
    test_graph = nx.Graph()
    test_graph.add_nodes_from(["A", "B", "C", "D", "E"])
    test_graph.add_weighted_edges_from([
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 3),
        ("B", "D", 1),
        ("B", "E", 3),
        ("C", "D", 4),
        ("C", "E", 5),
        ("D", "E", 1)
    ])
    pos = nx.spring_layout(test_graph)
    nx.draw(test_graph, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(test_graph, 'weight')
    nx.draw_networkx_edge_labels(test_graph, pos, edge_labels)
    plt.show()


if __name__ == "__main__":
    usage_example("D")
