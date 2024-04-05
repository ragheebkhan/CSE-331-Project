from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:
    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info

    class edge:
        def __init__(self, u, v, weight, capacity):
            self.u = u
            self.v = v
            self.weight = weight
            self.capacity = capacity
        def incweight(self):
            self.weight = sys.maxsize if self.weight+1 == self.capacity else self.weight+1
    def dijkstra(self, G, isp, client):
        prevs = [-1] * len(G)
        d = {idx : float("inf") for idx, v in enumerate(G)}
        R = [(0,isp)]
        while R:
            currdist, currnode = heapq.heappop(R)
            if currdist > d[currnode]:
                continue
            for neighbor in G[currnode]:
                weight = neighbor.weight
                dist = currdist + weight
                if dist<d[neighbor.v]:
                    d[neighbor.v] = dist
                    heapq.heappush(R, (dist, neighbor.v))
                    if neighbor.v != isp:
                        prevs[neighbor.v] = currnode
        path = []
        current = client
        while (current != -1):
            path.append(current)
            current = prevs[current]
        path = path[::-1]
        return path

    def calculate_paths(self):
        # Initialize empty list of paths
        paths = dict()
        edges = dict()
        
        G = [[] for i in range(len(self.graph))]
        for node in self.graph.keys():
            for edge in self.graph[node]:
                G[node].append(self.edge(node,edge,1,self.info["bandwidths"][node]+1))
                edges[f"{node},{edge}"] = G[node][-1] 
        
        # Create list of clients sorted by ascending alphas
        clients = sorted(self.info["list_clients"], key = lambda x: self.info["alphas"][x])
        for client in clients:
            paths[client] = self.dijkstra(G, self.isp, client)
            for i in range(len(paths[client])-1):
                edges[f"{paths[client][i]},{paths[client][i+1]}"].incweight()
                
        return paths

    def output_paths(self):
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """
        paths, bandwidths, priorities = self.calculate_paths(), {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
    
