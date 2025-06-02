import java.util.*;
class Solution {
    public int[] solution(String[] gems) {
        int n = gems.length;
        Set<String> gemTypes = new HashSet<>(Arrays.asList(gems));
        int m = gemTypes.size(); //보석 종류 개수 

        Map<String, Integer> findGem = new HashMap<>();
        int start = 0, end = 0;
        int minLen = Integer.MAX_VALUE;
        int answerStart = 0, answerEnd = 0;
        
        while(start < n) {
            while(end<n && findGem.size()<m) {
                findGem.put(gems[end], findGem.getOrDefault(gems[end], 0) + 1);
                end += 1;
            }
            
            if (findGem.size() == m) {
                if (end-start < minLen) {
                    minLen = end-start;
                    answerStart = start+1;
                    answerEnd = end;
                }
            }
            
            findGem.put(gems[start], findGem.get(gems[start])-1);
            if (findGem.get(gems[start]) == 0) {
                findGem.remove(gems[start]);
            }
            start += 1;
        }
        return new int[]{answerStart, answerEnd};
    }
}