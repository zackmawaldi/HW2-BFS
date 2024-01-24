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

## Breadth First Search (BFS)

Breadth First Search (BFS) is a graph search method that traverses nodes on a graph given a start node in a "layer first" fashion. This method of traversal allows for shortest path determination (in conjugation with dijkstra algorithm). Here, I wrote an implementation of both BFS and shortest path search using NetworkX package.

# Getting Started
To get started you will need to fork this repository onto your own github. You will then work on the code base from your own repo and make changes to it in the form of commits. 

# Reference Information
## Test Data
Two networks have been provided in an adjacency list format readable by [networkx](https://networkx.org/), is a commonly used python package for working with graph structures. These networks consist of two types of nodes:
* Faculty nodes 
* Pubmed ID nodes

However, since these are both stored as strings, you can treat them as equivalent nodes when traversing the graph. The first graph ("citation_network.adjlist") has nodes consisting of all BMI faculty members, the top 100 Pubmed papers *cited by* faculty, and the top 100 papers that *cite* faculty publications. Edges are directed and and edge from node A -> B indicates that node A *is cited by* node B. There are 5120 nodes and 9247 edges in this network.

The second network is a subgraph of the first, consisting of only the nodes and edges along the paths between a small subset of faculty. There are 30 nodes and 64 edges.

# Completing the assignment
Make sure to push all your code to github, ensure that your unit tests are correct, and submit a link to your github through the google classroom assignment.

# Grading

## Code (6 points)
* Breadth-first traversal works correctly (3)
* Traces the path from one faculty to another (2)
* Handles edge cases (1)

## Unit tests (3 points)
* Output traversal for mini data set (1)
* Tests for at least two possible edge cases (1)
* Correctly uses exceptions (1)

## Style (1 points)
* Readable code with clear comments and method descriptions
* Updated README with description of your methods

