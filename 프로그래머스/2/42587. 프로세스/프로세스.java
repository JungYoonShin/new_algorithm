import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> queue = new LinkedList<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for(int i=0; i<priorities.length; i++) {
            queue.add(new int[]{priorities[i], i});
            pq.add(priorities[i]);
        }
        int answer = 1;
        while(!queue.isEmpty()) {
            int[] p = queue.poll();
            if(pq.peek() > p[0]) {
                queue.add(p);
            }
            
            else {
                pq.poll();
                if(p[1] == location) {
                    return answer;
                }
                answer ++;
            }
        }
         
        return 0;
    }
}