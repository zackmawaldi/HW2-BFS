# write tests for bfs
import pytest
import random
import networkx as nx
from search import graph

def test_bfs_traversal():
    """
    Unit test for a breadth-first traversal.
    """
    
    """ Edge Case Checks """
    # Empty graph check
    empty = graph.Graph('data/empty.adjlist')
    assert empty.bfs('Foo') == []

    # No node in graph check
    tiny_network = graph.Graph('data/tiny_network.adjlist')

    with pytest.raises(nx.exception.NetworkXError):
        tiny_network.bfs('Foo')
    
    
    """ BFS traversal checks using networkx in-house BFS """
    #      Our BFS function                    Ground truth BFS from networkx
    assert tiny_network.bfs('Nevan Krogan') == list(nx.bfs_tree(tiny_network.graph, 'Nevan Krogan'))
    assert tiny_network.bfs('Luke Gilbert') == list(nx.bfs_tree(tiny_network.graph, 'Luke Gilbert'))
    assert tiny_network.bfs('Lani Wu') == list(nx.bfs_tree(tiny_network.graph, 'Lani Wu'))


def test_bfs():
    """
    Unit test for your breadth-first search.
    """
    
    """ Known not-conected graph where BFS output should be None """
    nx_disconnected = nx.DiGraph()
    nx_disconnected.add_nodes_from(['A','B','C','D','E','F','G','H'])
    nx_disconnected.add_edges_from([('A','B'),('B','C'),('B','D'),('B','F'),('G','H'), ('G', 'E')])

    # stub file input to avoid crashes
    disconnected = graph.Graph('data/empty.adjlist')

    # remove stub graph with our desired graph
    disconnected.graph = nx_disconnected

    # Do the call on the no path graph between A -> E
    assert disconnected.bfs('A', end='E') == None


    """ BFS shortest paths tests using networkx in-house BFS """
    full_network = graph.Graph('data/citation_network.adjlist')
    node_list = list(full_network.graph.nodes)
    
    # Idea is: try 10 times to find shortest paths between two random nodes. Awnsers should match, except when
    # there are two equal-in-distance paths. Then do extra checks
    for _ in range(10):
        source = random.choice(node_list)
        target = random.choice(node_list)

        # NetworkX throws an exception when there is no path.
        # Handel it by setting it to None (Just like our function)
        try:
            true_path = nx.shortest_path(full_network.graph, source=source, target=target)
        except nx.exception.NetworkXNoPath:
            true_path = None
        
        our_bfs = full_network.bfs(source, end=target)

        # If answers don't match, check lenghts are same, and if NX thinks it's a path. If not, assert error.
        if not true_path == our_bfs:
            if len(true_path) != len(our_bfs) or not nx.is_path(full_network.graph, our_bfs):
                assert true_path == our_bfs