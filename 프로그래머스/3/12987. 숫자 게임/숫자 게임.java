import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;

        Integer[] AInteger = Arrays.stream(A).boxed().toArray(Integer[]::new);
        Integer[] BInteger = Arrays.stream(B).boxed().toArray(Integer[]::new);
        
        Arrays.sort(AInteger, Collections.reverseOrder());
        Arrays.sort(BInteger, Collections.reverseOrder());
        
        int idx = 0;
        for(int i = 0; i < AInteger.length; i++) {
            if(BInteger[idx] > AInteger[i]) {
                idx++;
                answer++;
            }
        }
        return answer;
    }
}