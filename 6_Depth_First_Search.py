

from typing import List

class Solution:
    def dfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        def dfs(node):

            visited.add(node)
            dfs_traversal.append(node)
            
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        visited = set()  
        dfs_traversal = []  
        
        dfs(0)
        
        return dfs_traversal
        
