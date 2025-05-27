import java.util.Map;
import java.util.HashMap;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        Map<Character, Integer> map = new HashMap<>();
        
        int i = 0;
        for(char c : skill.toCharArray()) {
            map.put(c, i++); 
        }
        
        
        for(String s : skill_trees) {
            char[] t = s.toCharArray();
            Boolean check = true;
            i = 0;
            
            for(Character c : t) {
                if(map.containsKey(c)) {
                    if(map.get(c) == i) {
                        i++;
                    }
                    else {
                        check = false;
                        break;
                    }
                }
            }
            
            if(check) {
                answer++;
            }
        }
        return answer;
    }
}