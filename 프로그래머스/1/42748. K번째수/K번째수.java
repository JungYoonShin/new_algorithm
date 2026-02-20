import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        
        for(int[] command: commands) {
            List<Integer> a = new ArrayList<>();
            for(int i=command[0]-1; i<command[1]; i++){
                a.add(array[i]);
            }
            
            Collections.sort(a);
            answer.add(a.get(command[2]-1));
        }
        return answer.stream().mapToInt(i->i).toArray();
    }
}