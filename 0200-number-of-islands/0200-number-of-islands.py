class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL = len(grid),len(grid[0])

        count = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(i,j,grid)
        return count

    def dfs(self, i,j,grid):
        if i<0 or i>=len(grid):
            return
        if j<0 or j>=len(grid[0]):
            return
        if grid[i][j] == "#" or grid[i][j] == "0":
            return
        grid[i][j]= "#"

        self.dfs(i+1,j,grid)
        self.dfs(i-1,j,grid)
        self.dfs(i,j+1,grid)
        self.dfs(i,j-1,grid)

        