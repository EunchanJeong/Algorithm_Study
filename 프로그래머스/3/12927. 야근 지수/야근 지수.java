import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int work : works) {
            pq.add(work);
        }
        
        for(int i = 0; i < n; i++) {
            int workMax = pq.poll();
            
            if(workMax == 0) {
                break;
            }
            
            pq.add(workMax - 1);
            
        }
        
        for(int remain : pq) {
            answer += remain * remain;
        }
        return answer;
    }
}