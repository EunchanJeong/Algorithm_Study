import java.util.Arrays;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        Character[] t = new Character[s.length()];
        
        int i = 0;
        for(char c : s.toCharArray()) {
            t[i++] = c;
        }
        
        Arrays.sort(t,  Collections.reverseOrder());
        
        for(char c : t) {
            answer += c;
        }
        return answer;
    }
}