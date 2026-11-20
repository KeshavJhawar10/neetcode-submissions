class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        total = 0
        
        adj_matrix = [[] for _ in range(n)]
        for u, v in edges:
            adj_matrix[u].append(v)
            adj_matrix[v].append(u)
        visited = set()
        def dfs(num):
            if num in visited:
                return 
            visited.add(num)
            for nei in adj_matrix[num]:
                dfs(nei)
                    
            
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                total +=1
        return total
        
     
