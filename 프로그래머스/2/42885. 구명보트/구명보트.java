import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        HashSet<int[]> set = new HashSet<>();
        Arrays.sort(people);
        
        int start = 0;
        int end = people.length - 1;
        
        while (start <= end) {
            if (people[start] + people[end] > limit) {
                end--;
            } else {
                start++;
                end--;
            }
            answer++;
        }

        return answer;
    }
}