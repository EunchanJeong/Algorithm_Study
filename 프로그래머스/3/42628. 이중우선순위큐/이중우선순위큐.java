import java.util.Queue;
import java.util.PriorityQueue;
import java.util.Comparator;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        
        Queue<Integer> minQueue = new PriorityQueue<>();
        Queue<Integer> maxQueue = new PriorityQueue<>(Comparator.reverseOrder());
        
        for(String o : operations) {
            String[] tmp = o.split(" ");
            
            if(tmp[0].equals("I")) {
                minQueue.offer(Integer.parseInt(tmp[1]));
                maxQueue.offer(Integer.parseInt(tmp[1]));
            }
            else if(tmp[0].equals("D")) {
                if (minQueue.isEmpty()) {
                    continue;
                }
                
                int num = Integer.parseInt(tmp[1]);
                
            
                if(num == 1) {
                    int n = maxQueue.poll();
                    minQueue.remove(n);
                }
                else {
                    int n = minQueue.poll();
                    maxQueue.remove(n);
                }
            }
        }
        
        if(!minQueue.isEmpty() && !maxQueue.isEmpty()) {
            answer[0] = maxQueue.poll();
            answer[1] = minQueue.poll();
        }
        else if(minQueue.isEmpty() && !maxQueue.isEmpty()) {
            answer[0] = maxQueue.poll();
            answer[1] = 0;
        }
        else if(!minQueue.isEmpty() && maxQueue.isEmpty()) {
            answer[0] = 0;
            answer[1] = minQueue.poll();
        }
        else {
            answer[0] = 0;
            answer[1] = 0;
        }
        
        return answer;
    }
}