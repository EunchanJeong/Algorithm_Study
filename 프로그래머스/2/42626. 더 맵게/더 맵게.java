import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        int result = 0;
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for(int s : scoville) {
            minHeap.add(s);
        }
        
    
        while(minHeap.size() >= 2) {
            
            int s1 = minHeap.poll();
            
            if(s1 >= K) {
                break;
            }
            
            int s2 = minHeap.poll();

            result = s1 + (s2 * 2);
            minHeap.add(result);

            answer++;
        }
        
        result = minHeap.poll();
        
        return result >= K ? answer : -1;
    }
}