from graph import Graph

# Create the graph object
graph = Graph('../data/citation_network.adjlist')

# Visualize and save the graph with BFS traversal starting from 'Lani Wu'
graph.visualize('graph_visualization.png', bfs_start='Lani Wu')

# Visualize and save the graph with the shortest path from 'Luke Gilbert' to '30944313'
graph.visualize('shortest_path_visualization.png', bfs_start='Lani Wu', bfs_end='Marina Sirota')
