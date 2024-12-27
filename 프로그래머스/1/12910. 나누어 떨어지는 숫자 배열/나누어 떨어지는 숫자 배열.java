import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> answerList = new ArrayList<>();
        
        for(int a : arr) {
            if(a % divisor == 0) {
                answerList.add(a);
            }
        }
        
        if(answerList.isEmpty()) {
            return new int[] { -1 };
        }
        Collections.sort(answerList);
        return answerList.stream().mapToInt(i -> i).toArray();
    }
}