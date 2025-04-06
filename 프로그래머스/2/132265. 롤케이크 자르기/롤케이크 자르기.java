import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        Set<Integer> A = new HashSet<>();
        Map<Integer, Integer> B = new HashMap<>();
        
        for(int t : topping) {
            B.put(t, B.getOrDefault(t, 0) + 1);
        }
        for(int i = 0; i < topping.length; i++) {
            A.add(topping[i]);
            
            B.put(topping[i], B.get(topping[i]) - 1);
            
            if(B.get(topping[i]) == 0) {
                B.remove(topping[i]);
            }
            
            if(A.size() == B.size()) {
                answer++;
            }
        }
      
        return answer;
    }
}