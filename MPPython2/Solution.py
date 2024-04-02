from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:
    def bfs(self, G, s, t):
        priors = [-1] * len(G)
        visited = [False] * len(G)
        queue = deque()
        queue.append(s)
        visited[s] = True
        while queue:
            node = queue.popleft()
            for i in range(len(G[node])):
                if visited[i] == False and G[node][i] > 0:
                    queue.append(i)
                    visited[i] = True
                    priors[i] = node
        
        path = []
        current = t
        while (current != -1):
            path.append(current)
            current = priors[current]
        path = path[::-1]
        if path == [t]:
            return None
        return path
    
    def residual_graph(self, G, f):
        Gf = [[0 for i in range(len(G))] for i in range(len(G))]
        for idxi, i in enumerate(G):
            for idxj, j in enumerate(i):
                if j != 0 and f[idxi][idxj] < j:
                    Gf[idxi][idxj] = j - f[idxi][idxj]
                if j != 0 and f[idxi][idxj] > 0:
                    Gf[idxj][idxi] = f[idxi][idxj]
        return Gf
    

    def augment(self, f, P, G):
        fprime = f.copy()
        capacities = []
        for idx, i in enumerate(P):
            if idx+1 < len(P):
                capacities.append(G[i][P[idx+1]]-f[i][P[idx+1]])
        b = min(capacities)
        for idx, i in enumerate(P):
            if idx+1 < len(P):
                if G[i][P[idx+1]] != 0:
                    fprime[i][P[idx+1]] += b
                else:
                    fprime[P[idx+1]][i] -= b
        return fprime
        
    def MaxFlow(self, G, s, t):
        f = [[0 for i in range(len(G))] for i in range(len(G))]
        Gf = self.residual_graph(G,f)
        P = self.bfs(Gf,s,t)
        while P != None:
            f = self.augment(f,P,G)
            Gf = self.residual_graph(G, f)
            P = self.bfs(Gf,s,t)
        return f

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
        test = [[0,0,0,0,0,0,0,0,0,8,8,0],
                [0,0,7,0,7,7,0,0,0,0,7,float("inf")],
                [0,4,0,4,4,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,1,0,1,1,0,float("inf")],
                [0,2,2,0,0,0,0,2,0,0,0,0],
                [0,4,0,0,0,0,4,0,4,0,0,0],
                [0,0,0,1,0,1,0,0,0,0,0,float("inf")],
                [0,0,0,0,1,0,0,0,0,0,0,float("inf")],
                [0,0,0,5,0,5,0,0,0,0,0,float("inf")],
                [1,0,0,1,0,0,0,0,0,0,0,0],
                [7,7,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0]]
        print(self.MaxFlow(test,0,11))
        
        # Convert graph to adjacency matrix and set weight/capacity for each edge
        # For each packet/customer
        #   Run dijkstra's algorithm to find path
        #   Update weight of each edge in path. Add 0 if there is capacity left, add 1, if not
        
        

        paths, bandwidths, priorities = {}, {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
