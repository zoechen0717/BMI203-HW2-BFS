import networkx as nx

# Load the graph from the adjacency list file
file_path = "../data/citation_network.adjlist"
#citation_network.adjlist
#tiny_network.adjlist
 # Replace with the actual path to your file
graph = nx.read_adjlist(file_path, create_using=nx.DiGraph, delimiter=";")

# Use networkx.bfs_tree to find the shortest path
source = "34533455"
target = "Marina Sirota"

try:
    # Create a BFS tree from the source node
    bfs_tree = nx.bfs_tree(graph, source=source)

    # Find the shortest path in the BFS tree
    shortest_path = nx.shortest_path(bfs_tree, source=source, target=target)
    print(f"Shortest path from '{source}' to '{target}': {shortest_path}")
except nx.NetworkXNoPath:
    print(f"No path found from '{source}' to '{target}'.")
except nx.NodeNotFound as e:
    print(e)


# Generate the BFS tree and extract traversal order
bfs_tree = nx.bfs_tree(graph, source=source)
bfs_traversal_order = list(bfs_tree.nodes)

# Print the BFS traversal order
print(f"BFS Traversal Order starting from '{source}':")
print(bfs_traversal_order)
