import queue
import networkx as nx

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

    def bfs(self, start, end=None):
        """
        Performs a breadth first traversal and pathfinding on graph G

        Args:
        start: start node
        end (optional): end node

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        graph = self.graph

        if type(graph) != type(nx.DiGraph()):
            raise TypeError(f"You're graph is of type {type(graph)} not {type(nx.Graph())}")

        q = queue.Queue()
        visited = set()

        distances = {start: (0,[start], None)}
                    # node: (distance, path, parent)
        
        q.put(start)
        visited.add(start)
        while q.qsize() != 0:
            vertix = q.get()
            neighbors = list(graph.neighbors(vertix)) # list casting is to avoid a wierd bug...

            for n in neighbors:
                if n not in visited:
                    visited.add(n)
                    q.put(n)

                    # retrive runtime by getting parent path + current node n
                    new_path = distances[vertix][1] + [n]
                    dis = len(new_path) - 1
                    distances[n] = (dis, new_path, vertix)
                    
                    # If we found the end goal, return it
                    if end and n == end:
                        return distances[n][1]

        # if we finish bfs and didn't hit earlier if return, return None (end not found by bfs)
        # else, just return bfs visit path (as a list, per requirment)
        if end:
            return None
        else:
            return list(visited)