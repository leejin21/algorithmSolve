class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
                return
            if grid[i][j] == "0":
                # if this position is water
                return
            
            # note this land is visited -> turn into water
            grid[i][j] = "0"
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        land = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # if this position is land
                    # print(i, j)
                    dfs(i, j)
                    land += 1
                # print(land)
        return land