import java.util.*;

class Solution {
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    
    public int solution(int[][] maps) {        
        int n = maps.length;
        int m = maps[0].length;
        
        return bfs(new int[]{0, 0}, maps, n, m);
    }
    
    private int bfs(int[] coord, int[][] maps, int n, int m) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offerLast(coord);
        int[][] visited = new int[n][m];
        visited[coord[0]][coord[1]] = 1;
        
        while (!queue.isEmpty()) {
            int[] c = queue.removeFirst();
            int x = c[0];
            int y = c[1];
            
            if (x == n - 1 && y == m - 1) {
                return visited[x][y];
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || nx > n - 1 || ny < 0 || ny > m - 1 || visited[nx][ny] != 0) {
                    continue;
                }
                
                if (maps[nx][ny] == 1) {
                    queue.offerLast(new int[]{nx, ny});
                    visited[nx][ny] = visited[x][y] + 1;
                }
            }
        }
        
        return -1;
    }
}