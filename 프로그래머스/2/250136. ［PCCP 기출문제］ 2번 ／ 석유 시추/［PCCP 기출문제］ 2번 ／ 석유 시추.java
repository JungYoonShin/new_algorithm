import java.util.*;
class Solution {
    int[] dx = {0, 0, -1, 1};
    int[] dy = {-1, 1, 0, 0};
    
    int bfs(boolean[][] visited, int x, int y, int color, int row, int col, int[][] land, int[][] graph) {
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{x, y});
        visited[x][y] = true;
        graph[x][y] = color;
        int[] s = null;
        int cnt = 1;
        
        while(!q.isEmpty()) {
            s = q.poll();
            for(int d=0; d<4; d++) {
                int nx = s[0] + dx[d];
                int ny = s[1] + dy[d];
                if (0 <= nx && nx < row && 0 <= ny && ny < col) {
                    if(land[nx][ny] == 1 && visited[nx][ny] == false) {
                        q.add(new int[]{nx, ny});
                        cnt++;
                        visited[nx][ny] = true;
                        graph[nx][ny] = color;
                    }
                }
            }
            
        }
        return cnt;
        
    }
    
    public int solution(int[][] land) {
        int answer = 0;
        
        int row = land.length;
        int col = land[0].length;
        boolean[][] visited = new boolean[row][col];
        int[][] graph = new int[row][col];
        HashMap<Integer, Integer> colorAndLand = new HashMap<>();
        
        int color = 1;
        for(int i=0; i<row; i++) {
            for(int j=0; j<col; j++) {
                if(visited[i][j] == false && land[i][j] == 1) {
                    int s = bfs(visited, i, j, color, row, col, land, graph);
                    colorAndLand.put(color, s);
                    color++;
                }
            }
        }
    
        
        List<Integer> result = new ArrayList<>();
        
        for(int j=0; j<col; j++) {
            HashSet<Integer> set = new HashSet<>();
            for(int i=0; i<row; i++) {
                if(graph[i][j] != 0) {
                    set.add(graph[i][j]);
                }
            }
            int size = 0;
            for(Integer a : set) {
                size += colorAndLand.get(a);
            }
            result.add(size);
        }
        
        return Collections.max(result);
    }
}