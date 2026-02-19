import java.util.*;
class Solution {
    
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    
    int bfs(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        boolean[][] visited = new boolean[n][m];
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0, 1});
        visited[0][0] = true;
        int[] status = null;
        boolean flag = false;
        while(!q.isEmpty()) {
            status = q.poll();
            if(status[0] == n-1 && status[1] == m-1) {
                return status[2];
            }
            for(int i=0; i<4; i++) {
                int nx = status[0] + dx[i];
                int ny = status[1] + dy[i];
                
                if(0<=nx && nx<n && 0<=ny && ny < m){
                    if(maps[nx][ny] == 1 && visited[nx][ny] == false) {
                        visited[nx][ny] = true;
                        q.add(new int[]{nx, ny, status[2]+1});
                    }
                }
            }
        }
        return -1;
    }
    
    public int solution(int[][] maps) {
        int answer = 0;
        return bfs(maps);
    }
}