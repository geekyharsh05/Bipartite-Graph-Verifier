import argparse

def is_bipartite(graph):
    """
    Check if a given graph is bipartite.

    Args:
        graph (dict): An adjacency list representation of the graph.

    Returns:
        bool: True if the graph is bipartite, False otherwise.
    """
    if not isinstance(graph, dict):
        raise ValueError("Input graph must be represented as an adjacency list (dictionary).")

    nodes = set(graph.keys())
    for neighbors in graph.values():
        if not isinstance(neighbors, list):
            raise ValueError("Each node's neighbors must be represented as a list.")
        nodes.update(neighbors)

    if len(nodes) != len(graph):
        raise ValueError("Graph must be a simple graph without self-loops or multiple edges between the same nodes.")

    if not all(isinstance(node, int) for node in nodes):
        raise ValueError("All nodes must be integers.")

    if not graph:
        return True  # An empty graph is considered bipartite

    n = len(graph)
    color = [None] * n

    for start in range(n):
        if color[start] is None:
            color[start] = 0
            stack = [start]

            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if color[neighbor] is None:
                        color[neighbor] = 1 - color[current]
                        stack.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return False

    return True

def main():
    """
    Command-line interface for verifying if a graph is bipartite.
    """ 
    parser = argparse.ArgumentParser(description="Bipartite Graph Verification CLI")
    parser.add_argument("-n", "--nodes", type=int, required=True, help="Number of nodes")

    args = parser.parse_args()

    try:
        n = args.nodes
        graph = {i: list(map(int, input(f"Enter neighbors of node {i} (space-separated): ").split())) for i in range(n)}
    except ValueError:
        print("Error: Please enter valid integers for node neighbors.")
        return

    try:
        is_bipartite_result = is_bipartite(graph)
        result = "bipartite" if is_bipartite_result else "not bipartite"
        print(f"The graph is {result}.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
