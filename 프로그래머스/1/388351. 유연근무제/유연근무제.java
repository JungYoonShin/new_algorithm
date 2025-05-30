class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        
        //주말 인덱스 
        int saturday_idx = (6-startday);
        int sunday_idx = (7-startday);
    
        for (int j=0; j<schedules.length; j++) {
            boolean flag = true;
            for (int i=0; i<=6; i++) {
                
                int today = (startday - 1 + i) % 7;

                if (today == 5 || today == 6) continue;
                                   
                int hour = schedules[j] / 100;
                int minute = schedules[j] % 100 + 10;

                if (minute >= 60){
                    hour += 1;
                    minute -= 60;
                }

                int time = hour * 100 + minute;

                if(timelogs[j][i] > time) {
                    flag= false;
                    System.out.println(timelogs[j][i]);
                    break;
                }
            }
            if(flag) {
                answer+=1;
            }
        }     
        
        return answer;
    }
}