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

    def dprime(self, w, G, R, d):
        dists = []
        for node in R:
            if G[node][w] == 0:
                continue
            dists.append((node, w, d[node]+G[node][w]))
        return min(dists, key = lambda x: x[2])
    
    def dijkstra(self, G, s):
        priors = [-1] * len(G)
        R = [s]
        d = {s : 0}
        queue = deque()
        queue.append(s)
        while queue:
            curr = queue.popleft()
            neighbors = []
            for node in R:
                for idx, neighbor in enumerate(G[node]):
                    if neighbor != 0 and idx not in R:
                        neighbors.append(idx)
            if neighbors == []:
                break
            w = []
            for n in neighbors:
                w.append(self.dprime(n,G,R,d))
            w = min(w, key = lambda x: x[2])
            R.append(w[1])
            d[w[1]] = w[2]
            priors[w[1]] = w[0]
            for node in R:
                for idx, neighbor in enumerate(G[node]):
                    if neighbor != 0 and idx not in R:
                        queue.append(idx)

        paths = [0] * len(G)
        for idx, node in enumerate(G):
            path = []
            curr = idx
            while curr != -1:
                path.append(curr)
                curr = priors[curr]
            path = path[::-1]
            paths[idx] = path
        return paths

            

    def output_paths(self):
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """
        adj_matrix = [[0,0,0,0,0,0,0,0,0,1,1],
                      [0,0,1,0,1,1,0,0,0,0,1],
                      [0,1,0,1,1,0,0,0,0,0,0],
                      [0,0,1,0,0,0,1,0,1,1,0],
                      [0,1,1,0,0,0,0,1,0,0,0],
                      [0,1,0,0,0,0,1,0,1,0,0],
                      [0,0,0,1,0,1,0,0,0,0,0],
                      [0,0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,1,0,0,0,0,0],
                      [1,0,0,1,0,0,0,0,0,0,0],
                      [1,1,0,0,0,0,0,0,0,0,0]]
        
        

        paths, bandwidths, priorities = {}, {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
