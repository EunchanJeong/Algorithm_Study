import java.util.Arrays;
class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        
        int start = 0;
        int end = 0;
        int range = 2 * w + 1;
        int diff = 0;
        int cur = 1;
        
        for(int station : stations) {
            start = station - w;
            end = station + w;
            
            if(cur < start) {
                diff = start - cur;
                
                if(diff%range == 0) {
                    answer += diff/range;
                }
                else {
                    answer += diff/range + 1;
                }
            }
            cur = end + 1;
        }
        
        if(cur <= n) {
            diff = n - cur + 1;
            
            if(diff%range == 0) {
                    answer += diff/range;
                }
                else {
                    answer += diff/range + 1;
                }
        }
        return answer;
    }
}