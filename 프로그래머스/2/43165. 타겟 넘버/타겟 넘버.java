import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        
        List<Integer> leaves = new ArrayList<>();
        
        leaves.add(0);
        int answer = 0;
        
        for(int num : numbers) {
            List<Integer> tmp = new ArrayList<>();
            
            for(int leaf : leaves) {
                tmp.add(leaf + num);
                tmp.add(leaf - num);
            } 
            
            leaves = tmp;
        }
        
        for(int leaf : leaves) {
            if(leaf == target) {
                answer++;
            }
        }
        
        return answer;
    }
}