#User function Template for python3
from typing import List
from collections import deque

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        visited = set()
        queue = deque([0])
        
        bfs_traversal = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                bfs_traversal.append(node)
                
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        
        return bfs_traversal
