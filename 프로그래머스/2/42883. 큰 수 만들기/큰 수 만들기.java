import java.util.*;
class Solution {
    public String solution(String number, int k) {
        String answer = "";
        
        Stack<Character> stack = new Stack<>();
        int delete = 0;
        
        for(int i=0; i<number.length(); i++) {
            if (stack.empty()) {
                stack.push(number.charAt(i));
            } else{
                while(!stack.empty() && stack.peek() < number.charAt(i) && delete < k) {
                    stack.pop();
                    delete++;
                }
                stack.push(number.charAt(i));
            }
        }
        
        char[] result = new char[number.length()-k];
        
        for(int i=0; i<number.length()-k; i++) {
            result[i] = stack.get(i);
        }
        
        
        return new String(result);
    }
}