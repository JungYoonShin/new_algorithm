import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        List<double[]> answer = new ArrayList<>();
        HashMap<Integer, Integer> people = new HashMap<>();
        
        for(int stage: stages) {
            people.putIfAbsent(stage, 0);
            people.put(stage, people.get(stage)+1);
        }
        
        int cnt = stages.length;
        for(int i=1; i<N+1; i++) {
            if(!people.containsKey(i)) {
                answer.add(new double[]{i, 0});
            } else {
                
                answer.add(new double[]{i, (double) people.get(i)/cnt});
                cnt -= people.get(i);
            }
        }
        
        answer.sort((a, b) -> {
            if(b[1] == a[1]) {
                return (int) (a[0] - b[0]);
            }
            return Double.compare(b[1], a[1]);
        });
        
        int[] result = new int[N];
        int i=0;
        for(double[] a : answer) {
            result[i] = (int) a[0];
            i++;
        }
        

        return result;
    }
}