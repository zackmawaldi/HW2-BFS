# Assignment 2
Breadth-first search

# Assignment Overview
The purpose of this assignment is to get you comfortable working with graph structures and to implement a breadth-first search function to traverse the graph and find the shortest path between nodes.

# Assignment Tasks

## Coding Assessment
In search/graph.py:
* [X] Define the function bfs that takes in a graph, start node, and optional node and:
	* [X] If no end node is provided, returns a list of nodes in order of breadth-first search traversal from the given start node
	* [X] If an end node is provided and a path exists, returns a list of nodes in order of the shortest path to the end node
	* [X] If an end node is provided and a path does not exist, returns None
* [X] Be sure that your code can handle possible edge cases, e.g.:
	* [X] running bfs traversal on an empty graph
	* [X] running bfs traversal on an unconnected graph
	* [X] running bfs from a start node that does not exist in the graph
	* [X] running bfs search for an end node that does not exist in the graph
	* [X] any other edge cases you can think of 

In test/test_bfs.py:
* [X] Write unit tests for breadth-first traversal and breadth-first search 
* [X] You may use the two networks provided in the data folder or create your own for testing
* [X] Test at least 2 possible edge cases (listed above)
* [X] Include a test case that fails and raises an exception

[![HW2 - BFS](https://github.com/zackmawaldi/HW2-BFS/actions/workflows/test.yml/badge.svg)](https://github.com/zackmawaldi/HW2-BFS/actions/workflows/test.yml)

# Breadth First Search (BFS)

Breadth First Search (BFS) is a graph search method that traverses nodes on a graph given a start node in a "layer first" fashion. This method of traversal allows for shortest path determination (in conjugation with dijkstra algorithm). Here, I wrote an implementation of both BFS and shortest path search using NetworkX package.