import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        return bfs(maps);
    }
    
    int bfs(int[][] maps) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        int n = maps.length;
        int m = maps[0].length;
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        q.add(new int[]{0, 0, 1});
        visited[0][0] = true;
        
        while(!q.isEmpty()){
            int now[] = q.poll();
            if (now[0] == n-1 && now[1] == m-1){
                return now[2];
            }
            
            for(int i=0; i<4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];
                
                if ((nx>=0  && nx<n && ny>=0 && ny<m) && !visited[nx][ny] && maps[nx][ny] != 0) {
                    visited[nx][ny] = true;
                    q.add(new int[]{nx, ny, now[2] + 1});
                }
            }
        }
        
        return -1;
    }
}