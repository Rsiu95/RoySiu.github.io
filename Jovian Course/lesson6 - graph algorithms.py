import sys
'''
Representing a graph:
A node is generally the "point" at which you would like to visit
An edge is the "path" between 2 points.

i.e. general graph data structure

    0 ----- 1 
    |      /|\
    |    /  |  \
    |   /   |   2
    |  /    |  /
    | /     | /
    4 ----- 3

Note that the numbers represent nodes and are just labels, the lines between each are
the edges
'''
# to represent the above structure
num_nodes = 5
# edges are bidirectional here, order also doesn't matter
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3,4)]

# A better way to create the graph
# build an adjanceny list

'''

Using the above structure, we track the nodes and store their immediate neighbours

0 --> 1, 4
1 --> 0, 2, 3, 4
2 --> 1, 3
3 --> 1, 2, 4
4 --> 0, 1, 3

'''

# Create a class to represent a graph as an adjacency list:

class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        
        # create the adjacency list, which is empty to be filled
        self.adjacency_list = [[] for _ in range(num_nodes)]
        
        # insert the edge into the appropriate list
        for node1, node2 in edges:
            # Add both nodes to each other as it is a bidirectional graph
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)
    
    # create a repr function to display the adjacency list more elegantly        
    def __repr__(self):
        return "\n".join(["{}: {}".format(node, neighbours) for \
            node, neighbours in enumerate(self.adjacency_list)])
        
    def __str__(self):
        return self.__repr__()
    
    # write a function to add an edge to a graph represented as an adjacency list
    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)
    
    # write a function to remove an edge from a graph represented as an adjacency list
    def remove_edge(self, node1, node2):
        
        # check if there is an edge between node 1 and node 2
        if node2 in self.adjacency_list[node1]:
            self.adjacency_list[node1].remove(node2)
        
        # same as above since it's bidirectional/undirected    
        if node1 in self.adjacency_list[node2]:
            self.adjacency_list[node2].remove(node1)
            
graph1 = Graph(num_nodes, edges)
print("Adjacency List")
print(graph1)

# Adjacency Matrix
'''
    0 ----- 1 
    |      /|\
    |    /  |  \
    |   /   |   2
    |  /    |  /
    | /     | /
    4 ----- 3

first we create a matrix n*n, where n = no. nodes in the graph.
To represent above graph as a matrix
      0  1  2  3  4
    0 0  1  0  0  1
    1 1  0  1  1  1
    2 0  1  0  1  0
    3 0  1  1  0  1
    4 1  1  0  1  0
    
Where a 1 in this matrix represent that there is an edge between the 2 nodes. i.e. node
0 and 1 has an edge.
'''

class Adjacency_Matrix:
    
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        
        # initialise an n * n matrix of 0
        self.adjacency_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
        
        # insert a 1 if there is an edge
        for node1, node2 in edges:
            # Add both nodes to each other as it is a bidirectional graph
            self.adjacency_matrix[node1][node2] = 1
            self.adjacency_matrix[node2][node1] = 1
    
    def __repr__(self):
        return "\n".join(str(row) for row in self.adjacency_matrix)
        
    def __str__(self):
        return self.__repr__()
    
    def add_edge(self, node1, node2):
        self.adjacency_matrix[node1][node2] = 1
        self.adjacency_matrix[node2][node1] = 1
        
    def remove_edge(self, node1, node2):
        self.adjacency_matrix[node1][node2] = 0
        self.adjacency_matrix[node2][node1] = 0
    
graph2 = Adjacency_Matrix(num_nodes, edges)
print(graph2)
print("\n")
graph2.add_edge(1,1)
print("Adjacency Matrix")
print(graph2)
graph2.remove_edge(1,1)
print("\n")
print(graph2)

# Graph Traversal
# Breadth-First Serach (BFS) -> use a queue (first in first out)

'''
Implement BFS given a source node in a graph
    0 ----- 1 
    |      /|\
    |    /  |  \
    |   /   |   2
    |  /    |  /
    | /     | /
    4 ----- 3
    
'''

def bfs(graph, root):
    queue = []
    visited = [False] * len(graph.adjacency_list)
    
    visited[root] = True
    distance = [None] * len(graph.adjacency_list)
    parent = [None] * len(graph.adjacency_list)
    
    queue.append(root)
    distance[root] = 0
    idx = 0
    
    while idx < len(queue):
        # get first element that was just inserted and not dequeued
        current = queue[idx]
        idx += 1
        
        for node in graph.adjacency_list[current]:
            if not visited[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                visited[node] = True
                queue.append(node)
    return queue, distance, parent
print('\n')
print(graph1)
# supposedly i need to keep a print graph1 statement before i print bfs because of
# how stdout works in python apparently...? odd...
print(bfs(graph1, 3))
print('\n')

#num_nodes3 = 9
#edges3 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]

# Write a program to check if all the nodes in a graph are connected

# depth-first search (DFS) - use a stack (last in last out)

def dfs(graph, root):
    stack = []
    visited = [False] * len(graph.adjacency_list)
    result = []
    # pushing these into stack first, don't want to label as visited until we pop from stack
    stack.append(root)
    
    while len(stack) > 0:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(current)
            
            for node in graph.adjacency_list[current]:
                stack.append(node)
        
    return result

print(graph1)

print(dfs(graph1,3))
print('\n')

# write a function to detect a cycle in a graph
# a cycle is a path where the original node paths back to itself i.e. in the above
# diagram, 1, 4, 3 is a cycle

# TODO


# weighted graphs

num_nodes5 = 9
# (node1, node2, weight)
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

# directed graphs,
num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]

# define a class to represent weighted and directed graphs

class Graph:
    def __init__(self, num_nodes, edges, directed = False, weighted = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        
        for edge in edges:
            if self.weighted:
                # include weights
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                # exclude weights
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)
                    
    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}: {}\n".format(i, nodes)
        return result
    
    def __str__(self):
        return self.__repr__()
    
graph2 = Graph(num_nodes5, edges5, weighted = True)
print(graph2)
graph3 = Graph(num_nodes6, edges6, directed = True)
print(graph3)