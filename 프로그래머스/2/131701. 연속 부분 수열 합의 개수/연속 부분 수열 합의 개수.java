import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

class Solution {
    public int solution(int[] elements) {
        
        int n = elements.length;
        int[] extend = new int[n * 2];
        
        for(int i = 0; i < extend.length; i++) {
            if(i < n) {
                extend[i] = elements[i];
            }
            else {
                extend[i] = elements[i - n];
            }
        }
        
        Set<Integer> set = new HashSet<>();
        
        for(int i = 1; i < n+1; i++) {
            for(int j = 0; j < n; j++) {
                int sumNum = Arrays.stream(extend, j, j + i).sum();
                
                set.add(sumNum);
            }
        }
        
        
        return set.size();
    }
}