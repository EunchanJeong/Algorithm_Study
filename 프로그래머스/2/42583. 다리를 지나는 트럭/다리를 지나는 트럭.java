import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        Queue<Integer> bridgeOn = new LinkedList<>();
        for(int i = 0; i < bridge_length; i++) {
            bridgeOn.add(0);
        }
        
        Queue<Integer> bridgeOut = new LinkedList<>();
        
        Queue<Integer> trucks = new LinkedList<>();
        for(int t : truck_weights) {
            trucks.add(t);
        }
        
        int time = 0;
        int cur = 0;
        
        while(bridgeOut.size() < truck_weights.length) {
            time++;
            
            int out = bridgeOn.poll();
            cur -= out;
            
            if(!trucks.isEmpty()) {
                int t = trucks.peek();
                
                if(cur + t <= weight) {
                    trucks.poll();
                    bridgeOn.add(t);
                    cur += t;
                }
                else {
                    bridgeOn.add(0);
                }
            }
            else {
                    bridgeOn.add(0);
            }
            
            if(out != 0) {
                bridgeOut.add(out);
            }
        }
        
        return time;
    }
}