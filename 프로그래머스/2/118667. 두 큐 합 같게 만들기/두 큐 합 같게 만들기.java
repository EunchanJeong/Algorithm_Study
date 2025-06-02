import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = -1;
        
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        
        long qSum1 = 0;
        long qSum2 = 0;
        
        for(int i : queue1) {
            q1.add(i);
            qSum1 += i;
        }
        
        for(int i : queue2) {
            q2.add(i);
            qSum2 += i;
        }
        
        int count = 0;
        
        while(count <= queue1.length * 4) {
            if(qSum1 > qSum2) {
                int poll = q1.poll();
                q2.add(poll);
                
                qSum1 -= poll;
                qSum2 += poll;
            }
            else if(qSum1 < qSum2) {
                int poll = q2.poll();
                q1.add(poll);
                
                qSum2 -= poll;
                qSum1 += poll;
            }
            else if(qSum1 == qSum2) {
                answer = count;
                break;
            }
            
            count++;
        }
        
        return answer;
    }
}