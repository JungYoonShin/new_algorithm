import java.util.*;
class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {};
        int sum = 0;
        int end = 0;
        
        ArrayList<int[]> result = new ArrayList<>();
        
        for(int start=0; start<sequence.length; start++) {
            while(sum < k && end < sequence.length) {
                sum += sequence[end];
                end++;
            }
            if(sum == k) {
                result.add(new int[]{start, end-1, (end-1-start)});
            }
            
            sum -= sequence[start];
        }
    
        
        result.sort((a, b) -> {
            if(a[2] == b[2]) {
                return a[0] - b[0];
            }
            return a[2] - b[2];
        });
            
        // for (int[] arr : result) {
        //     System.out.println(Arrays.toString(arr));
        // }
        
        int[] first = result.get(0);
        
        return new int[]{first[0], first[1]};
    }
}