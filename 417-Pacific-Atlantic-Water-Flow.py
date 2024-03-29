class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
                return []
    
        # List which will have both the coordinates
        pacific = set()
        atlantic = set()
        # Get the number of rows and columns
        m,n = len(matrix), len(matrix[0])

        # Define left, right, up, down
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        # Define the dfs traversal
        def dfs(visited, x,y):
            visited.add((x,y))
            for dx, dy in directions:
                new_x, new_y  = x + dx, y + dy

                # If the coordinates are valid and if c(i) > c (i-1)
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and matrix[new_x][new_y] >= matrix[x][y]:
                    dfs (visited, new_x, new_y)

        # Iterate for rows
        for i in range(m):
            dfs(pacific, i , 0)
            dfs(atlantic, i, n-1)

        # Iterate for columns
        for j in range(n):
            dfs(pacific, 0 , j)
            dfs(atlantic, m-1, j)

        # Return the matching coordinates
        return list(pacific.intersection(atlantic))