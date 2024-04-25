from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys
import time

class Solution:

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
        ct = time.time()
        loads = [0] * len(self.graph)

        bfs_paths = bfs_path(self.graph,self.isp,self.info["list_clients"])
        for client in bfs_paths.keys():
            for path_node in bfs_paths[client]:
                if path_node == self.isp or path_node == client:
                    continue
                newload = loads[path_node] + 1
                loads[path_node] = newload
                node_bw = self.info["bandwidths"][path_node]
                if newload > node_bw:
                    node_bw += 1
                    self.info["bandwidths"][path_node] = node_bw
        paths, bandwidths, priorities = bfs_paths, self.info["bandwidths"], {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        et = time.time()
        print(et - ct)
        return (paths, bandwidths, priorities)
