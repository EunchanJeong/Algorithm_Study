import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        
        Map<String, Integer> carIn = new HashMap<>();
        Map<String, Integer> carOut = new HashMap<>();
        
        int baseTime = fees[0];  
        int baseFee = fees[1];           
        int unitTime = fees[2];     
        int unitFee = fees[3];
        
        int i = 0;
        for(String record : records) {
            String[] r = record.split(" ");
            String car = r[1];
            int time = getTime(r[0]);
            
            if(r[2].equals("IN")) {
                carIn.put(car, time);
            }
            else if(r[2].equals("OUT")) {
                carOut.put(car, carOut.getOrDefault(car, 0) + (time - carIn.get(car)));
                carIn.remove(car);
            }
        }
        
        int lastTime = 23 * 60 + 59;
        for (String car : carIn.keySet()) {
            int t = lastTime - carIn.get(car);
            
            if (carOut.containsKey(car)) {
                    
                    carOut.replace(car, carOut.get(car) + t);    
            } 
            else {
                carOut.put(car, t);
            }   
        }
        
        Object[] sortKey = carOut.keySet().toArray();
        Arrays.sort(sortKey);
        
        int[] answer = new int[sortKey.length];

        for(i = 0; i < answer.length; i++) {
            int result = baseFee;
            String car = String.valueOf(sortKey[i]);
            
            int t = carOut.get(car);
      
            int fee = baseFee;
            if (t > baseTime) {
                fee += (int) Math.ceil((t - baseTime) / (double) unitTime) * unitFee;
            }
            answer[i] = fee;
        }
        
        return answer;
    }
    
    public int getTime(String time) {
        String[] t = time.split(":");
        
        int hour = Integer.parseInt(t[0]) * 60;
        int minute = Integer.parseInt(t[1]);
        return hour + minute;
    }
}