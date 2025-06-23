import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        
        Map<Character, Integer> counts = new HashMap<>();
        
        int index = 0;
        for(char c : s.toCharArray()) {
            if(counts.containsKey(c)) {
                answer[index] = index - counts.get(c);
            }
            else {
                answer[index] = -1;
            }
            
            counts.put(c, index);
            index++;
        }
        return answer;
    }
}