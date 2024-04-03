from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:
    class edge:
        def __init__(self, u, v, weight):
            self.u = u
            self.v = v
            self.weight = weight

    def adj_list_with_weights(self):
        """
        Creates adjacency list with weights
        """
        G = [[]] * len(self.graph.keys())

        for key in self.graph.keys():
            for neighbor in self.graph[key]:
                new_edge = self.edge(key,neighbor,0)
                G[key].append(new_edge)

        return G
    
    def dprime(self, w, G, R, d):
        edges_to_w = []
        for node in R:
            for edge in G[node]:
                if edge.v == w:
                    edges_to_w.append(edge)
        min = edges_to_w[0]
        for edge in edges_to_w:
            if d[edge.u]+edge.weight < d[min.u]+min.weight:
                min = edge
        return (min, d[min.u]+min.weight)

    def dijkstra(self, G, s):
        R = [s]
        d = {s : 0}
        queue = deque()
        queue.append(s)
        all_neighbors = []
        for neighbor in G[s]:
            all_neighbors.append(neighbor)
        while all_neighbors != []:
            w = []
            for neighbor in all_neighbors:
                if neighbor.v in R:
                    continue
                w.append(self.dprime(neighbor.v,G,R,d))
            w = min(w, key = lambda x: x[1])
            R.append(w[0].v)
            d[w[0].v] = w[1]
            all_neighbors.clear()
            for i in R:
                for n in G[i]:
                    if n.v not in R:
                        all_neighbors.append(n)

        return d
        
    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info

    def output_paths(self):
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """
        """
        G = [[0 for i in range(len(self.graph))] for i in range(len(self.graph))]
        for key in self.graph.keys():
            for i in self.graph[key]:
                G [key][i] = self.info["bandwidths"][key]
        """
        test = [[self.edge(0,9,8),self.edge(0,10,8)],
                [self.edge(1,2,7),self.edge(1,4,7),self.edge(1,5,7),self.edge(1,10,7)],
                [self.edge(2,1,7),self.edge(2,3,7),self.edge(2,4,7)],
                [self.edge(3,2,1),self.edge(3,6,1),self.edge(3,8,1),self.edge(3,9,1)],
                [self.edge(4,1,2),self.edge(4,2,2),self.edge(4,7,2)],
                [self.edge(5,1,4),self.edge(5,6,4),self.edge(5,8,4)],
                [self.edge(6,3,1),self.edge(6,5,1)],
                [self.edge(7,4,1)],
                [self.edge(8,3,4),self.edge(8,5,5)],
                [self.edge(9,0,1),self.edge(9,3,1)],
                [self.edge(10,0,7),self.edge(10,1,7)]]
        for i in test:
            for j in i:
                j.weight = 1
        print(self.dijkstra(test,0))

        paths, bandwidths, priorities = {}, {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
