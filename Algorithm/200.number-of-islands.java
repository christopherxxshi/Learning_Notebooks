/*
 * @lc app=leetcode id=200 lang=java
 *
 * [200] Number of Islands
 *
 * https://leetcode.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (40.61%)
 * Total Accepted:    326.1K
 * Total Submissions: 798.5K
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of
 * islands. An island is surrounded by water and is formed by connecting
 * adjacent lands horizontally or vertically. You may assume all four edges of
 * the grid are all surrounded by water.
 * 
 * Example 1:
 * 
 * 
 * Input:
 * 11110
 * 11010
 * 11000
 * 00000
 * 
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * 11000
 * 11000
 * 00100
 * 00011
 * 
 * Output: 3
 * 
 */
class Coordinate{
    public int x, y;
    public Coordinate(int x, int y){
        this.x = x;
        this.y = y;
    }
}
class Solution {
    public int numIslands(char[][] grid) {
        if(grid == null || grid.length ==  0 || grid[0].length == 0){
            return 0;
        }
        int n = grid.length;
        int m = grid[0].length;
        int ans = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] == '1'){
                    BFS(grid, i, j);
                    ans++;
                }
            }
        }
        return ans;
    }
    private void BFS(char[][] grid, int x, int y){
        Queue<Coordinate> q = new LinkedList<>();
        q.offer(new Coordinate(x, y));
        int[] dirX = {0, 0, 1, -1};
        int[] dirY = {1, -1, 0, 0};
        
        
        while(!q.isEmpty()){
            Coordinate curCoor = q.poll();
            for(int i = 0 ; i < 4; i++){
                Coordinate newCoor = new Coordinate(
                    curCoor.x + dirX[i],
                    curCoor.y + dirY[i]
                );
                if(!isBound(newCoor, grid)){
                    continue;
                }
                if(grid[newCoor.x][newCoor.y] == '1')
                {
                    grid[newCoor.x][newCoor.y] = '0';
                    q.offer(newCoor);
                }
            }
        }
    }
    private boolean isBound(Coordinate coor, char[][] grid){
        int n = grid.length;
        int m = grid[0].length;
        return 0 <= coor.x && coor.x < n && 0 <= coor.y && coor.y < m; 
    }
}

