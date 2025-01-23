import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function

    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None): #def BFS(G, source):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # This Breadth-first search method is based on the psedo code provided in the Lecture slides(slide #24-38)
        # I also take some ideas from this classic bfs post writen in C++: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
        # Some edge cases I can think about to raise errors
        # Running bfs traversal on an empty graph
        if len(self.graph) == 0:
            raise ValueError("The graph is empty.")
        # Running BFS from a start node that does not exist in the graph
        if start not in self.graph:
            raise ValueError("Start node invalid.")
        # Running BFS from a invalid end node
        if end is not None and end not in self.graph:
            raise ValueError("End node invalid.")

        # Q = queue() ---> initialize queue
        Q = deque() # "deque() will make the queue process much faster" ---> from the geekforgeek post
        # visited = [ ] ---> initialize list of visited nodes
        visited = []
        #If an end node is provided and a path exists, returns a list of nodes in order of the shortest path to the end node
        history = {start: None} # We need this path history to reconstruct the visited nodes for the shortest path

        # Q.push(source) ---> Push source node to queue
        Q.append(start)
        # visited.append(source) ---> Mark source node as visited
        visited.append(start)

        # Loop through nodes in graph
        while Q: # while Q is not empty:
            v = Q.popleft() # v = Q.pop(), deque.popleft() = list.pop() but much faster

            # Here we need to somehow detour from the psedo code
            # We need to consider the case that a end node provided and we need to reconstruct the shortest path.
            if v == end:
                path = []
                while v is not None:
                    path.append(v)
                    v = history[v] # The path history of the visited nodes for the shortest path
                return path[::-1]  # It's a queue so we need to reverse the order to ouput the right path

            # Explore neighbors
            N = self.graph.neighbors(v) # N = neighbors(v)
            for w in N : # for all w in N:
                if w not in visited: # if w not in visited:
                    visited.append(w) # visited.append(w)
                    history[w] = v
                    Q.append(w) # Q.push(w)

        # If there is an end node input and a path does not exist, return None
        if end is not None:
            return None

        # If there's no end node input, return a list nodes with the order of BFS traversal
        return visited
