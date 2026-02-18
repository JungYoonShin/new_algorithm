import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> stack = new ArrayDeque<>();
        
        for(int i=0; i<progresses.length; i++) {
            int left = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
            stack.add(left);
        }
        
        int a = stack.peek();
        int num = 0;
        while(!stack.isEmpty()) {
            int top = stack.poll();
            if(a >= top) {
                num++;
            }
            else{
                answer.add(num);
                num = 1;
                a = top;
            }
        }
        answer.add(num);
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}