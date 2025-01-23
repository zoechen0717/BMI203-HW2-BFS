from graph import Graph

def main():
    # Create an instance of the Graph class with the tiny_network.adjlist file
    graph = Graph('../data/citation_network.adjlist')
    #citation_network.adjlist
    #tiny_network.adjlist

    # Test BFS for pathfinding between two nodes
    print("\n'Lani Wu':")
    path = graph.bfs('34533455')
    print(path)


    # Test BFS for pathfinding between two nodes
    print("\nShortest path from 'Lani Wu' to 'Marina Sirota':")
    shortest_path = graph.bfs('34533455', 'Marina Sirota')
    print(shortest_path)

    # Test BFS with a node that doesn't exist
    try:
        print("\nBFS Traversal starting from an invalid node:")
        graph.bfs('InvalidNode')
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
