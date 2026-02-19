import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        HashMap<String, Integer> map = new HashMap<>();
        HashMap<String, ArrayList<String>> singo = new HashMap<>();
        HashSet<String> set = new HashSet<>(Arrays.asList(report));
        
        for (String r : set) {
            String[] split = r.split(" ");
            String from = split[0];
            String to = split[1];

            map.put(to, map.getOrDefault(to, 0) + 1);

            singo.putIfAbsent(from, new ArrayList<>());
            singo.get(from).add(to);
        }
        
        ArrayList<Integer> block = new ArrayList<>();
        for(String s: id_list) {
            int cnt = 0;
            if (!singo.containsKey(s)) {
                block.add(0);
            }
            else {
                for(String b : singo.get(s)) {
                    if(map.get(b) >= k) {
                        cnt++;
                    }
                }
                block.add(cnt);
            }
        }
        return block.stream().mapToInt(i->i).toArray();
    }
}