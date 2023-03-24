class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # Create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        # Visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        # If ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # If it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # Mark as being visited
        visited[i] = -1
        # Visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        # After visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True