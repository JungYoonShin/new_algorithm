import java.util.*;
class Solution {
    ArrayList<int[]> route = new ArrayList<>();
    
    void find_route(ArrayList<Integer> current,
                    int n,
                    boolean[] visited) {

        if (current.size() == n) {

            int[] temp = new int[n];
            for (int i = 0; i < n; i++) {
                temp[i] = current.get(i);
            }

            route.add(temp);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {

                visited[i] = true;
                current.add(i);

                find_route(current, n, visited);

                current.remove(current.size() - 1);
                visited[i] = false;
            }
        }
    }
    
    int find_dungeons(int[] route, int k, int[][] dungeons) {
        int cnt = 0;
        for(int i=0; i<route.length; i++) {
            if(dungeons[route[i]][0] <= k) {
                k -= dungeons[route[i]][1];
                cnt++;
            }
        }
        return cnt;
    }
    
    
    public int solution(int k, int[][] dungeons) {
        int answer = -1;
        int n = dungeons.length;
        boolean[] visited = new boolean[n];
        
        find_route(new ArrayList<>(), n, visited);
        ArrayList<Integer> result = new ArrayList<>();
        
        for(int i=0; i<route.size(); i++) {
            result.add(find_dungeons(route.get(i), k, dungeons));
        }
        
        
        return Collections.max(result);
    }
}