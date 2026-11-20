class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(num):
            if num in visited:
                return

            visited.add(num)

            for nei in adj[num]:
                dfs(nei)

        for u, v in reversed(edges):
            # Temporarily remove edge
            adj[u].remove(v)
            adj[v].remove(u)

            visited = set()
            dfs(u)

            # Check if all nodes are connected
            if len(visited) == n:
                return [u, v]

            # Restore edge
            adj[u].append(v)
            adj[v].append(u)

        return []