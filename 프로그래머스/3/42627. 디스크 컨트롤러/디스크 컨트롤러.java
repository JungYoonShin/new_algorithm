import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        Map<Integer, List<int[]>> job = new HashMap<>();
        for(int i=0; i<jobs.length; i++){
            job.putIfAbsent(jobs[i][0], new ArrayList<>());
            job.get(jobs[i][0]).add(new int[]{i, jobs[i][1]});
        }
        
        int time = 0;
        int[] disk = null;
        PriorityQueue<int[]> pq = new PriorityQueue<>(
        (a, b) ->
            a[0] != b[0] ? a[0] - b[0] :
            a[1] != b[1] ? a[1] - b[1] :
                           a[2] - b[2]
        );
        
        int finish = 0;
        
        while(finish < jobs.length) {
            
            if(disk != null && disk[0] == time) {
                disk = null;
            }
            
            if(job.containsKey(time)) {
                for(int[] j: job.get(time)) {
                    pq.add(new int[]{j[1], time, j[0]});
                }
            }
            
            if (disk == null && !pq.isEmpty()) {
                int[] cur = pq.poll();
                int cost = cur[0];
                int request = cur[1];

                disk = new int[]{time + cost, request};
                answer += (time + cost) - request;
                finish++;
            }
            
            time ++;
            
        }
        return answer / jobs.length;
    }
}