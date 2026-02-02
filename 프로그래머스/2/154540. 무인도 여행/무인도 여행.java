import java.util.*;
class Solution {
    boolean[][] visited;
    int food = 0;
    public int[] solution(String[] maps) {
        int[] answer = {};
        int n = maps.length;
        int m = maps[0].length();
        visited = new boolean[n][m];
        char[][] map = new char[n][m];
        
        for (int i = 0; i < n; i++) {
            map[i] = maps[i].toCharArray();
        }
        
        List<Integer> result = new ArrayList<>();
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(!visited[i][j] && map[i][j] != 'X'){
                    food = 0;
                    dfs(visited, map, i, j);
                    result.add(food);
                }
            }
        }
        
        Collections.sort(result);
        if(!result.isEmpty()){
            return result.stream().mapToInt(Integer::intValue).toArray();
        }
        return new int[]{-1};
    }
    
    void dfs(boolean[][] visited, char[][] maps, int x, int y) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        int n = maps.length;
        int m = maps[0].length;
        visited[x][y] = true;
        food += maps[x][y] - '0';
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if((nx>=0 && nx<n && ny>=0 && ny<m) && !visited[nx][ny] && maps[nx][ny] != 'X') {
                dfs(visited, maps, nx, ny);
            }
        }
    }
    
    
}
